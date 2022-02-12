from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "大标题" #大标题
    embed.description = "详情 [链接](https://discordapp.com) ```\n备注```" #详情说明
    embed.add_field(name="Name of the field", value="This is an inline field content", inline=True) #小标题1
    embed.add_field(name="Name of the field", value="This is an another inline field content", inline=False) #小标题2
    embed.add_field(name="Not inline field", value="This is not an inline field content", inline=False) #小标题3
    embed.url = "https://google.com" #大标题的链接
    embed.colour = 0x4287f5 #0x留着，后面加颜色编号
    embed.set_author(name="作者名", url="https://google.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png") #开头作者相关
    embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png") #右上角的图
    embed.set_footer(text="脚注", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
    embed.set_image(url="https://www.funnynation.org/wp-content/uploads/2022/02/dc横幅3-scaled.gif") #主图大图

    return embed
