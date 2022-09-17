import discord
from discord.ext import commands
import os

description = "Sheeesh"
with open('token.txt', 'r') as f:
    for line in f: TOKEN = line
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

"""def query():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    with conn.cursor() as cur:
        cur.execute("SELECT now()")
        res = cur.fetchall()
        conn.commit()
        print(res)"""

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def orz(ctx):
    """Adds two numbers together."""
    await ctx.send('Orz Zeyu')

bot.run(TOKEN)