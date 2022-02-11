from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "就这？"
    embed.description = "咱就是说 [一整个无语的链接](https://discordapp.com) ```\n芜湖起飞```"
    embed.add_field(name="Name of the field", value="This is an inline field content", inline=True)
    embed.add_field(name="Name of the field", value="This is an another inline field content", inline=False)
    embed.add_field(name="Not inline field", value="This is not an inline field content", inline=False)
    embed.url = "https://google.com" #可以去掉
    embed.colour = 0x4287f5 #0x留着
    embed.set_author(name="Linbin Pang", url="https://google.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png") #右上角的图
    embed.set_footer(text="This is the footer", icon_url="https://cdn.discordapp.com/embed/avatars/0.png") #脚注
    embed.set_image(url="https://www.funnynation.org/wp-content/uploads/2022/02/dc横幅3-scaled.gif") #主图

    return embed
