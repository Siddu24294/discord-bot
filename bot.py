from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
import requests
import bot_commands
import discord
from discord.ext import commands


token="ODY3MTcwNTcyMDMxMzYxMDI0.YPdNhw.LERfmbC6EgeCMG5Hfe3ZKGCw9sE"
client=commands.Bot(command_prefix="#")


'''slash = SlashCommand(client, sync_commands=True)
id = 859739150512554004 #server id hear
guild_ids = [id]
@slash.slash(name="wallpaper", description="get your self wallpapers",
options=[create_option(
          name="wallpapers",
          description="what wallpapers do you want",
          option_type=6, #corresponds to USER
          required=False),
        create_option(
          name="nuber of wallpapers",
          description="number of wallpaper you want",
          option_type=3, #corresponds to STRING
          required=False),
        create_option(
          name="nuber of wallpapers",
          description="number of wallpaper you want",
          option_type=3, #corresponds to STRING
          required=False)
        ])
'''


@client.event
async def on_ready():
	print("bot is ready")


@client.command()
async def hello(ctx):
	await ctx.send("```hi```")


@client.command(aliases=['h','help'])
async def Help(ctx):
	await bot_commands.bthelp(ctx=ctx)


@client.command(aliases=['s'])
async def search(ctx,word,*,sentence):
	print(sentence)
	await ctx.send(word in sentence)
	await bot_commands.search(ctx=ctx,word=word,sentence=sentence)


@client.command(aliases=['w','wall','walls'])
async def wallpaper(ctx,number:int,*searchTerm):
	await bot_commands.wallpaper(ctx=ctx,searchTerm="+".join(searchTerm),shortlist=int(number))


@client.command()
async def anime(ctx):pass

client.run(token)