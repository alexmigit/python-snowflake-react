CREATE OR REPLACE TABLE fact_production AS
SELECT
    timestamp,
    status,
    machine_id,
    part_id,
    operator_id
FROM stg_log;