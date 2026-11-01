CREATE OR ALTER VIEW dbo.vw_daily_paid_claims AS
SELECT CAST(service_date AS date) AS service_date,
       COUNT(DISTINCT claim_id) AS claim_count, SUM(paid_amount) AS paid_amount_total
FROM dbo.claims_silver
WHERE claim_status = 'PAID'
GROUP BY CAST(service_date AS date);
