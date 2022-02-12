from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "狼人杀"
    embed.description = "本局游戏人数：5"
    embed.add_field(name="已加入游戏玩家", value="@user\n@user2\n@user3\n……", inline=False)
    embed.colour = 0xb647ff
    embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png") #右上角的图
    embed.set_footer(text="↓点击反应加入游戏", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

    return embed
