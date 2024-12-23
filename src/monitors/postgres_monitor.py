from .base_monitor import BaseMonitor
import psycopg2

class PostgresMonitor(BaseMonitor):
    def __init__(self, subscription_id):
        super().__init__(subscription_id)
        self.metrics = [
            'cpu_percent',
            'memory_percent',
            'storage_percent',
            'active_connections',
            'network_bytes_ingress',
            'network_bytes_egress'
        ]

    async def collect_system_metrics(self, connection_string):
        query = """
        SELECT 
            current_timestamp as timestamp,
            count(*) as active_connections,
            sum(conflicts) as conflicts,
            sum(deadlocks) as deadlocks,
            (sum(blks_hit) * 100.0 / nullif(sum(blks_hit) + sum(blks_read), 0)) 
                as cache_hit_ratio
        FROM pg_stat_database;
        """
        
        with psycopg2.connect(connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()

