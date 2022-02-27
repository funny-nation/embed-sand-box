from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "用户随机的数字是" #大标题
    embed.description = "[1,2,3]"  # 详情说明
    embed.colour = 0x42ffd3 #0x留着，后面加颜色编号

    return embed
