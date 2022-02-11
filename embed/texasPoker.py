from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "德州扑克牌局已建立" #大标题
    embed.description = "你需要有至少10元加入牌局" #详情说明
    embed.add_field(name="点击反应加入牌局", value="↓", inline=True) #小标题1
    embed.colour = 0x000000 #0x留着，后面加颜色编号
    embed.set_thumbnail(url="https://www.funnynation.org/wp-content/uploads/2022/02/德州.png") #右上角的图

    return embed
