import discord, os
from discord.ext import commands
from dotenv import load_dotenv
import ftc_events as evt
import ftc_scoring as scoring
from discord.ext.commands import CommandNotFound

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('Invalid command, dumbass.')
        return
    raise error

@bot.command(name='rank', help='Determines the rank of the team.')
async def get_rank(ctx, team):
    msg = scoring.get_rank(int(team))
    await ctx.send(msg)

@bot.command(name='scoring', help='The scoring for the FTC game')
async def get_scoring(ctx):
    await ctx.send('https://firstinspiresst01.blob.core.windows.net/first-game-changers/ftc/game-one-page.pdf')

@bot.command(name='peepeepoopoo', help='Ethan')
async def peepeepoopoo(ctx):
    await ctx.send('peepeepoopoo {}'.format(ctx.message.author.mention))

@bot.command(name='stats', help='Link to FTC Stats')
async def get_stats(ctx):
    await ctx.send('http://www.ftcstats.org/2021/index.html')

@client.event
async def on_message(message):
    if "https://tenor.com/view/sonic-shadow-love-pog-big-chungus-gif-16580004" in message.content:
        await client.delete_message(message)

bot.run(TOKEN)