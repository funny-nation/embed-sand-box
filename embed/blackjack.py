from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "21牌局已建立" #大标题
    embed.description = "入池金额为10.0元" #详情说明
    embed.add_field(name="点击反应加入牌局", value="↓", inline=False) #小标题1
    embed.colour = 0x000000 #0x留着，后面加颜色编号
    embed.set_thumbnail(url="https://www.funnynation.org/wp-content/uploads/2022/02/21点.png") #右上角的图

    return embed
