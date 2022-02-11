from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "匿名内容"  # 大标题
    embed.colour = 0x763cb5  # 0x留着，后面加颜色编号

    return embed
