import os

from pymongo import MongoClient

from discord_notifier import send_discord_update
from weather_data import charlotte_weather, port_washington_weather


# Use the MongoDB connection string
CONNECTION_STRING = os.environ["connection_string"]

# Establish a connection to my MongoDB database
client = MongoClient(CONNECTION_STRING)

# Access the existing database
db = client["weather"]

# Create a variable for the charlotte collection from the weather database
charlotte = db["charlotteNC"]

# Insert data from charlotte_weather into the charlotte collection from the weather database
charlotte.insert_one(charlotte_weather)

# Create a variable for the portWashingtonWI collection
port_washington = db["portWashingtonWI"]

# Insert data from port_washington_weather into the portWashington collection
port_washington.insert_one(port_washington_weather)

# Close the connection
client.close()

# Use the Discord Webhook URL from the MongoDB Weather Database server
DISCORD_WEBHOOK_URL = os.environ["discord_webhook_url"]

# Notify the MongoDB Weather Database server if there are any important weather updates
send_discord_update(url=DISCORD_WEBHOOK_URL)
