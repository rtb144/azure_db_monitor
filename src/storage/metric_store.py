import psycopg2
from datetime import datetime

class MetricStore:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    async def store_metrics(self, metrics_data):
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor() as cur:
                cur.executemany("""
                    INSERT INTO metrics.database_metrics 
                    (timestamp, server_name, server_type, metric_name, 
                     metric_value, unit, resource_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, metrics_data)

