from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "GHS小花园富豪榜" #大标题
    embed.description = "1: user - 100元 \n2：user - 99元 " #详情说明
    embed.colour = 0xfff18a #0x留着，后面加颜色编号

    return embed
