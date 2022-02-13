from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "狼人杀"   # 游戏名称
    embed.description = "本局游戏人数：5"  # 游戏人数（卡牌的总数量）
    embed.add_field(name="已加入游戏玩家", value="@user\n@user2\n@user3\n……", inline=False)
    embed.colour = 0xb647ff
    embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png") #右上角的图
    embed.set_footer(text="↓点击反应加入游戏")

    return embed
