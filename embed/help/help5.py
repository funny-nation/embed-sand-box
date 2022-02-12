from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "3 - 用户可以使用货币送礼物"
    embed.description = ""
    embed.add_field(name="", value="", inline=False)
    embed.colour = 0xff9900
    return embed
