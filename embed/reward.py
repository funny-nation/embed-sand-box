from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "{活动名称}领奖" #大标题
    embed.description = "参与{活动名称}的玩家可以领奖啦！" #详情说明
    embed.add_field(name="奖金{100}货币", value="↓点击反应申请领奖", inline=False) #小标题1
    embed.colour = 0xffa621 #0x留着，后面加颜色编号
    embed.set_thumbnail(url="https://www.funnynation.org/wp-content/uploads/2022/02/钱袋.png") #右上角的图

    return embed
