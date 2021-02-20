import logging

import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey
from urllib.parse import urlparse
import hashlib

# Initialize the Cosmos client
endpoint = "YOUR_COSMOSDB_ENDPOINT"
key = 'YOUR_COSMOS_DB_KEY=='

# <create_cosmos_client>
client = CosmosClient(endpoint, key)
database_name = 'YOUR_DB_NAME'
container_name = 'YOUR_CONTAINER_NAME'

db = client.get_database_client(database_name)
container = db.get_container_client(container_name)

def main(documents: func.DocumentList) -> str:
    if documents:
        #
        # Do your things here
        #
        
        logging.info("Nobody ever logs things")
