class AlertManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.alert_rules = {
            'high_cpu': {
                'query': """
                    SELECT avg(metric_value) 
                    FROM metrics.database_metrics 
                    WHERE metric_name = 'cpu_percent' 
                    AND timestamp > now() - interval '5 minutes'
                    AND server_name = %s
                """,
                'threshold': 80
            },
            'storage_critical': {
                'query': """
                    SELECT metric_value 
                    FROM metrics.database_metrics 
                    WHERE metric_name = 'storage_percent'
                    AND timestamp > now() - interval '5 minutes'
                    AND server_name = %s
                    ORDER BY timestamp DESC 
                    LIMIT 1
                """,
                'threshold': 90
            }
        }

