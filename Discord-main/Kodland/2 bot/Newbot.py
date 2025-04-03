import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def plus(ctx, a, b):
    await ctx.send(int(a) + int(b))    

@bot.command()
async def minus(ctx, a, b):
    await ctx.send(int(a) - int(b))    
    
@bot.command()
async def times(ctx, a, b):
    await ctx.send(int(a) * int(b))    
    
@bot.command()
async def divide(ctx, a, b):
    await ctx.send(int(a) / int(b))    
@bot.command()
async def cool(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
bot.run("MTI4NzAxNDU1MDU5MTI0MjMzMQ.Gowe5M.GXI2H6IrTnrCUIqBydz-vI1Orhfi_-EoCkGCeQ")