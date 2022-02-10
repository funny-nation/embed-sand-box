from dotenv import load_dotenv
from src.Robot import Robot
load_dotenv()

import os
token = os.environ.get("token")

client = Robot()
client.run(token)