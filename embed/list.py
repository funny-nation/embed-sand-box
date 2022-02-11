from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "GHS小花园富豪榜" #大标题
    embed.description = "富豪榜列表" #详情说明
    embed.colour = 0xfff18a #0x留着，后面加颜色编号

    return embed
