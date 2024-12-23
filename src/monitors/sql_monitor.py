from .base_monitor import BaseMonitor

class SQLMonitor(BaseMonitor):
    def __init__(self, subscription_id):
        super().__init__(subscription_id)
        self.metrics = [
            'cpu_percent',
            'memory_usage_percent',
            'storage_percent',
            'dtu_consumption_percent',
            'connection_successful',
            'deadlocks'
        ]

    async def collect_metrics(self, resource_group, server_name):
        resource_id = (f"/subscriptions/{self.subscription_id}/"
                      f"resourceGroups/{resource_group}/"
                      f"providers/Microsoft.Sql/servers/{server_name}")
        
        return await self.get_metrics(resource_id, self.metrics)

