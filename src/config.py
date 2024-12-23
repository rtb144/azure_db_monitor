import os

CONFIG = {
    'subscription_id': os.getenv('AZURE_SUBSCRIPTION_ID'),
    'postgres_connection': os.getenv('POSTGRES_CONNECTION_STRING'),
    'monitoring_interval': 60,  # seconds
    'retention_days': 30,
    'alert_receivers': ['admin@company.com'],
    'servers': {
        'sql': [
            {'resource_group': 'rg1', 'name': 'sql1'},
            {'resource_group': 'rg1', 'name': 'sql2'}
        ],
        'postgres': [
            {'resource_group': 'rg1', 'name': 'pg1'},
            {'resource_group': 'rg1', 'name': 'pg2'}
        ]
    }
}

