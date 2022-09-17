import discord
from discord.ext import commands
import os
from random import choice
from query import query as Q
from query import db_query

description = "Sheeesh"
TOKEN = os.getenv('TOKEN')
BASE_DIR = 'Videos/'
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

LANGUAGES = [
    'english'
]

DIFFICULTIES = [
    'easy',
    'medium',
    'hard'
]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def orz(ctx):
    """ORZ"""
    await ctx.send('Orz Zeyu')
    await ctx.send(Q('Videos/1.mp3'))
    return

@bot.command()
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("Please join a voice channel first.")
        return
    channel = ctx.message.author.voice.chanenl
    await channel.connect()
    return

@bot.command()
async def leave(ctx):
    if not ctx.message.guild.voice_client:
        await ctx.send("The bot is not in a voice channel.")
        return
    await ctx.message.guild.voice_client.disconnect()
    return

@bot.command()
async def quizme(ctx, language, difficulty):
    language, difficuly = language.lower(), difficulty.lower()
    if language not in LANGUAGES:
        await ctx.send("Please enter a valid language.")
        return
    if difficulty not in DIFFICULTIES:
        await ctx.send("Please enter a valid difficulty.")
        return
    await ctx.send("You are an orz lord.")
    DIR = os.path.join(BASE_DIR, language, difficulty)
    possible = []
    for root, dirs, files in os.walk(DIR, topdown=False):
        for file in files: possible.append(os.path.join(DIR, file))
    question_file = choice(possible)

    


bot.run(TOKEN)