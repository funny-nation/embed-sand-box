from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "4 - 用户可以用货币购买服务器VIP"
    embed.description = "指令：ghs 买vip （默认从V1开始买）"
    embed.add_field(name="VIP等级-所需金额-福利编号", value="VIP1-2000"
                                                  "\nVIP2-5000"
                                                  "\nVIP3-8000"
                                                  "\nVIP4-16000"
                                                  "\nVIP5-30000"
                                                  "\nVIP6-60000"
                                                  "\nVIP7-100000"
                                                  "\nVIP8-180000"
                                                  "\nVIP9-280000"
                                                  "\nVIP10-400000"
                                                  "\n精灵VIP-700000"
                                                  "\n水晶VIP-1000000"
                                                  "\n圣火VIP-2000000", inline=False)
    embed.colour = 0xff9900
    return embed
