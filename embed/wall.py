from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.description = "小贼：\n匿名信息匿名信息匿名信息匿名信息匿名信息匿名信息匿名信息"  # 详情说明
    embed.colour = 0x763cb5  # 颜色需要随机
    return embed
