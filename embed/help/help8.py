from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "8 - GHS小花园匿名墙"
    embed.description = "私信bot指令：匿名 匿名内容" \
                        "\nbot将发布你的匿名消息到GHS匿名墙" 
    embed.colour = 0xff9900
    return embed
