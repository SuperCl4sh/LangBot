import queue
import time
import discord
from discord.ext import commands
import time
import asyncio
import os
from random import choice
from query import query as Q
from query import update_points
from query import get_points
from linear_algebra import *

description = "Sheeesh"
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

queue = dict()

audio_path = None

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("Please join a voice channel first.")
        return
    if ctx.message.guild.voice_client == ctx.message.author.voice.channel:
        await ctx.send("Bot is already in your voice channel.")
        return
    channel = ctx.message.author.voice.channel
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
    if ctx.message.author in queue:
        await ctx.send("Finish your current challenge before starting a new one.")
        return
    language, difficuly = language.lower(), difficulty.lower()
    if language not in LANGUAGES:
        await ctx.send("Please enter a valid language.")
        return
    if difficulty not in DIFFICULTIES:
        await ctx.send("Please enter a valid difficulty.")
        return
    DIR = os.path.join(BASE_DIR, language, difficulty)
    possible = []
    for root, dirs, files in os.walk(DIR, topdown=False):
        for file in files: possible.append(os.path.join(DIR, file))
    question_file = choice(possible)
    await ctx.send(file=discord.File(question_file))
    queue[ctx.message.author] = [question_file, time.perf_counter()]
    CHECKPOINTS = [1, 2, 3, 5, 10]
    for i in range(10, 0, -1):
        if i in CHECKPOINTS and ctx.message.author in queue:
            await ctx.send("You have {} seconds remaining.".format(i))
        elif ctx.message.author not in queue:
            return
        await asyncio.sleep(1)
    if ctx.message.author not in queue:
        return
    queue.pop(ctx.message.author, None)
    await ctx.send("The time limit is up. You took too long!")
    return

@bot.command()
async def answer(ctx, *args):
    if ctx.message.author not in queue:
        await ctx.send("No quiz active. To begin one, use ?quizme [language] [difficulty].")
        return
    audio_path, start_time = queue[ctx.message.author]
    queue.pop(ctx.message.author, None)
    get_points(ctx.message.author.id)
    end_time = time.perf_counter() # Get end time before API query
    if end_time - start_time > 10:
        await ctx.send("An error occured. Please try again.")
        return
    user_ans, actual_ans = string_to_vector(' '.join([word.lower() for word in args])), string_to_vector(' '.join([paragraph.lower() for paragraph in Q(audio_path)]))
    score = get_score(user_ans, actual_ans, end_time - start_time)
    await ctx.send("You scored {}!".format(score))
    
    update_points(ctx.message.author.id, score)
    return

@bot.command()
async def xp(ctx):
    await ctx.send("You currently have {} xp.".format(get_points(ctx.message.author.id)))
    return

def get_score(A, B, total_time):
    return round((1 - total_time / 10) * (100 * pow(cosine_similarity(A, B), 2)))

bot.run(os.getenv("TOKEN")) 
