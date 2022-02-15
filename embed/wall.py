from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.description = "匿名名称：匿名信息"  # 详情说明
    embed.colour = 0x763cb5  # 颜色需要随机

    return embed
