import discord
import os, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f"images/{img_name}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTI4NzAxNDU1MDU5MTI0MjMzMQ.Gs8Tk8.MlsE99cjnCblaP9VRp-dhT3lSwYjMKWSMImeew")