from discord import Client, Embed, Message, Member, TextChannel
import importlib
import re

async def handleTestRequest(client: Client, message: Message):
    author: Member = message.author
    channel: TextChannel = message.channel
    if author == client.user:
        return

    if re.match("^show .+$", message.content):
        fileName = message.content[5:]
        try:
            targetModule = importlib.import_module("embed." + fileName, package=None)
            targetModule = importlib.reload(targetModule)
        except Exception:
            await channel.send(f"File \"{fileName}\" not found")
            return

        try:
            embed: Embed = targetModule.getEmbed()
            await channel.send(embed=embed)
            return
        except Exception as err:
            await channel.send(f"{err}")
            await channel.send(f"File \"{fileName}\" does not meet the requirement")
            return

