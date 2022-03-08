from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "您已签到成功"
    embed.description = "本次签到获得60货币！"
    embed.colour = 0xff9900
    return embed
