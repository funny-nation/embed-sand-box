from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "抢红包啦！\nuser_name的红包已经发出!" #大标题
    embed.description = "点击反应抢红包啦！"
    embed.add_field(name="恭喜user！", value="你抢到了100元", inline=False)
    embed.add_field(name="恭喜运气王user！", value="你抢到了最大的红包！100元！", inline=False)
    embed.colour = 0xff2121 #0x留着，后面加颜色编号
    embed.set_thumbnail(url="https://www.funnynation.org/wp-content/uploads/2022/02/红包.png") #右上角的图

    return embed
