from discord import Embed


def getEmbed() -> Embed:
    embed = Embed()
    embed.title = "This is title"
    embed.description = "Here is the description for this embed. The url is optional. "
    embed.url = "https://google.com"
    embed.colour = 0xFF0000
    embed.set_footer(text="This is the footer")
    embed.set_image(url="https://www.teenet.me/wp-content/uploads/2022/01/funnyNation.png")

    return embed
