import discord
import random
from bot_logic import gen_pass
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=discord.Intents.default)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(gen_pass(100))
    elif message.content.startswith('$bye'):
        await message.channel.send(gen_pass(100))
    else:
        await message.channel.send(message.content)

client.run("MTI4NzAxNDU1MDU5MTI0MjMzMQ.GEzt5d.gDhjVtqN5yKFZKiBLm6EylR1XDOUB7hhsMkLXM")
