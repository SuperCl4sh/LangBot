import discord
from discord.ext import commands
import os

description = "Sheeesh"
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def orz(ctx):
    """Adds two numbers together."""
    await ctx.send('Orz Zeyu')

bot.run(TOKEN)