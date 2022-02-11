from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "幸运抽奖" #大标题
    embed.description = "@user_name已发布抽奖活动！奖品是{奖品名称}" #详情说明
    embed.add_field(name="抽奖券{价格}/张，数量有限，只有{数量}个！", value="↓点击反应购买抽奖券参与抽奖", inline=False) #小标题3
    embed.colour = 0xe34bab #0x留着，后面加颜色编号
    embed.set_thumbnail(url="https://www.funnynation.org/wp-content/uploads/2022/02/宇宙素材-3.png") #右上角的图
    embed.set_footer(text="点击绿色反应开奖，点击红色反应关闭抽奖", icon_url="https://www.funnynation.org/wp-content/uploads/2022/02/宇宙素材-3.png")  # 脚注
    
    return embed
