from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "抢红包啦！" #大标题
    embed.description = "user_name的红包已经发出 ```\n点击反应抢红包啦！```" #详情说明
    embed.colour = 0xff2121 #0x留着，后面加颜色编号
    embed.set_thumbnail(url="https://www.funnynation.org/wp-content/uploads/2022/02/红包.png") #右上角的图

    return embed
