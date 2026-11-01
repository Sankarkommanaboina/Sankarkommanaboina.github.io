SELECT DATE(event_timestamp) AS event_date, service_area,
       COUNT(DISTINCT trip_id) AS trip_count,
       AVG(duration_minutes) AS avg_duration_minutes,
       SUM(distance_km) AS total_distance_km
FROM `YOUR_PROJECT.mobility.trips`
WHERE DATE(event_timestamp) BETWEEN @start_date AND @end_date
GROUP BY event_date, service_area;
