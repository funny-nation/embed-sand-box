from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "您的VIP升级啦！"
    embed.description = "恭喜@user晋升为尊贵的VIP10！记得常来玩儿哦！~"
    embed.colour = 0xf6d1ff
    embed.set_image(url="https://www.funnynation.org/wp-content/uploads/2022/02/圣火VIP.gif")

    return embed
