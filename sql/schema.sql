CREATE SCHEMA IF NOT EXISTS metrics;

-- Common metrics table
CREATE TABLE metrics.database_metrics (
    timestamp TIMESTAMPTZ NOT NULL,
    server_name VARCHAR(100),
    database_name VARCHAR(100),
    server_type VARCHAR(20),  -- 'sql' or 'postgres'
    metric_name VARCHAR(50),
    metric_value NUMERIC,
    unit VARCHAR(20),
    resource_id VARCHAR(255)
);

-- Create hypertable
SELECT create_hypertable('metrics.database_metrics', 'timestamp');

-- Indexes
CREATE INDEX idx_metrics_server ON metrics.database_metrics(server_name, timestamp DESC);
CREATE INDEX idx_metrics_type ON metrics.database_metrics(server_type, metric_name, timestamp DESC);

-- Continuous aggregates
CREATE MATERIALIZED VIEW metrics.hourly_metrics
WITH (timescaledb.continuous) AS
SELECT 
    time_bucket('1 hour', timestamp) AS hour,
    server_name,
    server_type,
    metric_name,
    AVG(metric_value) as avg_value,
    MAX(metric_value) as max_value,
    MIN(metric_value) as min_value
FROM metrics.database_metrics
GROUP BY 1, 2, 3, 4;

