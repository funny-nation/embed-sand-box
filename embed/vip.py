from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "您的VIP升级啦！"
    embed.description = "恭喜@user晋升为VIP10！记得常来玩儿哦！~"
    embed.colour = 0xbdf3ff
    embed.set_image(url="https://www.funnynation.org/wp-content/uploads/2022/02/圣火VIP.gif")

    return embed
