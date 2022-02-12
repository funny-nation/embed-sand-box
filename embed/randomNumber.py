from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "随机数字" #大标题
    embed.colour = 0x42ffd3 #0x留着，后面加颜色编号

    return embed
