import discord, os
from discord.ext import commands
from dotenv import load_dotenv
import ftc_events as evt

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='rank', help='Determines the rank of the team.')
async def get_rank(ctx, team):
    event = "2020/USGANGM4"
    rank, rp = evt.get_rank(event, team), evt.get_ranking_points(event, team)
    response = 'Team {} is rank {} with {} RP'.format(team, rank, rp)
    await ctx.send(response)

@bot.command(name='scoring', help='The scoring for the FTC game')
async def get_scoring(ctx):
    await ctx.send('https://firstinspiresst01.blob.core.windows.net/first-game-changers/ftc/game-one-page.pdf')

@bot.command(name='peepeepoopoo', help='Ethan')
async def peepeepoopoo(ctx):
    await ctx.send('peepeepoopoo')

bot.run(TOKEN)