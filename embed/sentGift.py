from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "叮！你有礼物哦请查收！" #大标题
    embed.description = "感谢 @喵喵喵 送给 @渡沿涼沂 的一辆RR幻影！两人正坐在车上往城市边缘开，还把车窗都摇下来~"
    embed.colour = 0xbdf3ff
    embed.set_image(url="https://www.funnynation.org/wp-content/uploads/2022/02/劳斯莱斯.png")

    return embed
