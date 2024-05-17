from quixstreams import Application  # import the Quix Streams modules for interacting with Kafka:
# (see https://quix.io/docs/quix-streams/v2-0-latest/api-reference/quixstreams.html for more details)

# import additional modules as needed
import random
import os
import json

# for local dev, load env vars from a .env file
from dotenv import load_dotenv
load_dotenv()

print("HELLO")
import os
for key, value in os.environ.items():
    print(f"{key}: {value}")


