from azure.identity import ManagedIdentityCredential
from azure.mgmt.monitor import MonitorManagementClient
import logging
from datetime import datetime, timedelta

class BaseMonitor:
    def __init__(self, subscription_id):
        self.credential = ManagedIdentityCredential()
        self.monitor_client = MonitorManagementClient(
            self.credential, 
            subscription_id
        )
        self.logger = logging.getLogger(__name__)

    async def get_metrics(self, resource_id, metric_names, timespan):
        try:
            return await self.monitor_client.metrics.list(
                resource_id,
                timespan=timespan,
                interval='PT1M',
                metricnames=','.join(metric_names)
            )
        except Exception as e:
            self.logger.error(f"Error fetching metrics: {str(e)}")
            raise

