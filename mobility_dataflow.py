# Apache Beam streaming: Pub/Sub JSON -> BigQuery
import argparse, json
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions

class ValidateTrip(beam.DoFn):
    def process(self, raw):
        try:
            x = json.loads(raw.decode("utf-8"))
            required = ["event_id","trip_id","event_timestamp","duration_minutes","distance_km","service_area"]
            if any(x.get(k) in (None,"") for k in required): raise ValueError("Missing required field")
            duration, distance = float(x["duration_minutes"]), float(x["distance_km"])
            if duration <= 0 or distance < 0: raise ValueError("Invalid duration or distance")
            yield {"event_id":str(x["event_id"]),"trip_id":str(x["trip_id"]),
                   "event_timestamp":str(x["event_timestamp"]),"duration_minutes":duration,
                   "distance_km":distance,"service_area":str(x["service_area"])}
        except Exception as exc:
            yield beam.pvalue.TaggedOutput("bad",{"raw_message":raw.decode("utf-8","replace"),"error":str(exc)})

def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_subscription",required=True)
    parser.add_argument("--output_table",required=True)
    parser.add_argument("--deadletter_table",required=True)
    args, pipeline_args = parser.parse_known_args(argv)
    opts = PipelineOptions(pipeline_args, streaming=True, save_main_session=True)
    opts.view_as(StandardOptions).streaming = True
    schema = "event_id:STRING,trip_id:STRING,event_timestamp:TIMESTAMP,duration_minutes:FLOAT,distance_km:FLOAT,service_area:STRING"
    bad_schema = "raw_message:STRING,error:STRING"
    with beam.Pipeline(options=opts) as p:
        parsed = (p | "Read" >> beam.io.ReadFromPubSub(subscription=args.input_subscription)
                    | "Validate" >> beam.ParDo(ValidateTrip()).with_outputs("bad",main="good"))
        (parsed.good | "WriteGood" >> beam.io.WriteToBigQuery(args.output_table,schema=schema,
          write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
          create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED))
        (parsed.bad | "WriteBad" >> beam.io.WriteToBigQuery(args.deadletter_table,schema=bad_schema,
          write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
          create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED))
if __name__ == "__main__": run()
