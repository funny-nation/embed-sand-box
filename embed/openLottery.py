from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "幸运抽奖" #大标题
    embed.description = "恭喜！@中奖人1 \n中奖人2 \n……" #详情说明
    embed.add_field(name="获得由@发奖人提供的奖品{奖品名称}", value="记得及时兑奖哦！", inline=False) #小标题3
    embed.colour = 0xe34bab #0x留着，后面加颜色编号
    embed.set_thumbnail(url="https://www.funnynation.org/wp-content/uploads/2022/02/宇宙素材-3.png") #右上角的图

    return embed
