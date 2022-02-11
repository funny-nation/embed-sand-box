from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "已开局摇骰子" #大标题
    embed.description = "本局每人可摇n颗骰子" #详情说明
    embed.add_field(name="点击反应参与对局", value="↓", inline=True) #小标题1
    embed.colour = 0x124dff #0x留着，后面加颜色编号
    embed.set_thumbnail(url="https://www.funnynation.org/wp-content/uploads/2022/02/cf278122b82bcd33.png") #右上角的图

    return embed
