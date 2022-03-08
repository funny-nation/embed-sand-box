from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "9 - 随机数字"
    embed.description = "玩家可以通过指令获取随机数字，数字范围和需要数字的数量只能是整数"
    embed.add_field(name="指令：ghs 随机数字 最小数字 最大数字 数字数量", value="例： ghs 随机数字 10 100 1", inline=False)
    embed.colour = 0xff9900
    return embed
