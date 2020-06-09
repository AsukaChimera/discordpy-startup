import discord
import random
client = discord.Client()
# ランダムで送るメッセージの一覧 ※ここに書き足すことでランダムに選ぶ内容を増やせる
random_contents = [
    "にゃーん",
    "わん！",
    "コケッコッコー",
]

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)


@client.event
async def on_message(message):
    # 送信者がbotである場合は弾く
    if message.author.bot:
        return
    # メッセージの本文が 鳴いて だった場合
    if message.content == "鳴いて":
        # 送信するメッセージをランダムで決める
        content = random.choice(random_contents)
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send(content)
    elif message.content == "ワンワン鳴いてみろよ":
        await message.channel.send("ﾜﾝ､ﾜﾝ…")


client.run("NzE5NDM1ODQxMzA2NDkyOTg4.Xt3tNg.j1W0xAFgAbykA7LJEEI2ITdswjM")