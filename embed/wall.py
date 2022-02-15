from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "匿名名称：匿名内容"  # 大标题里写
    embed.colour = 0x763cb5  # 颜色需要随机

    return embed
