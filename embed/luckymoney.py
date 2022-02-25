from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "user_name的红包已经发出!" #大标题
    embed.description = "抢到最大的红包的就是小傻瓜"
    embed.add_field(name="-", value="恭喜user！你抢到了100元！", inline=False)
    embed.add_field(name="-", value="恭喜user！你抢到了100元！", inline=False)
    embed.add_field(name="-", value="恭喜user！你抢到了100元！", inline=False)
    embed.add_field(name="恭喜运气王user！", value="你抢到了最大的红包！100元！", inline=False)
    embed.colour = 0xff2121 #0x留着，后面加颜色编号
    embed.set_thumbnail(url="https://www.funnynation.org/wp-content/uploads/2022/02/红包.png") #右上角的图
    embed.set_footer(text="↓点击反应抢红包")
    return embed
