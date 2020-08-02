#coding:UTF-8
# インストールした discord.py を読み込む
import discord
from discord.ext import tasks

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzM4NDU4NjYyMjI1MzEzODQy.XyMNOA.aZ0MijmJDiqpqf150SRouL_ODqo'
CHANNEL_ID = 737109573806063627

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@tasks.loop(seconds=7200)
async def loop():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('二時間経ちました。')

loop.start()
client.run(TOKEN)