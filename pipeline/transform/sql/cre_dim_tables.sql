CREATE OR REPLACE TABLE dim_machine AS
SELECT DISTINCT machine_id, type, location FROM stg_machines;

CREATE OR REPLACE TABLE dim_part AS
SELECT DISTINCT part_id, part_name, part_category FROM stg_parts;

CREATE OR REPLACE TABLE dim_operators AS
SELECT DISTINCT operator_id, name, shift FROM stg_operators;