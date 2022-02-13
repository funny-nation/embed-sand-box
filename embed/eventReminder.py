from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "活动名称"
    embed.url = "https://discord.gg/tB7ya5t7ze"  # 大标题的链接
    embed.description = "活动时间"  # 详情说明
    embed.add_field(name="活动详情", value="详情内容", inline=False)  # 小标题1
    embed.colour = 0xffdca8  # 0x留着，后面加颜色编号
    embed.set_footer(text="↓点击反应获取活动提醒")
    embed.set_image(url="https://www.funnynation.org/wp-content/uploads/2022/02/dc横幅3-scaled.gif")  # 主图大图

    return embed
