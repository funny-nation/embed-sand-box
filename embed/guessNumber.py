from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "猜数字游戏开始了！" #大标题
    embed.description = "范围是{1-100}哦！" #详情说明
    embed.add_field(name="点击反应参与游戏哦", value="↓", inline=True)  # 小标题1
    embed.colour = 0x124dff #0x留着，后面加颜色编号
    embed.set_thumbnail(url="https://www.funnynation.org/wp-content/uploads/2022/02/f459ab14864f7ecb.png") #右上角的图

    return embed
