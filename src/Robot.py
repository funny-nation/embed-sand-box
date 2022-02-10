import discord
from src.handleTestRequest import handleTestRequest
class Robot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        await handleTestRequest(self, message)
