# bot.py
import os
import random
import asyncio
import time

from discord.ext import commands
from boto.s3.connection import S3Connection

TOKEN = os.environ.get("DISCORD_TOKEN")


bot = commands.Bot(command_prefix="(A)")

@bot.command(name='clivage', help="Lance une partie du jeu du clivage, syntaxe : (A)clivage nb_de_mots delai")
async def clivage(ctx, nb_de_mots: int, delai: float):

	file = open("liste_francais.txt","r",encoding = "ISO-8859-15")

	words = file.readlines()

	for _ in range(nb_de_mots):

		response = random.choice(words)
		message = await ctx.send(response)
		await message.add_reaction('🇬')
		await message.add_reaction('🇩')
		await asyncio.sleep(delai)

	file.close()

	
@bot.command(name='barcelone36')
async def barcelone36(ctx):
	await ctx.send(f'https://fr.wikipedia.org/wiki/R%C3%A9volution_sociale_espagnole_de_1936')


bot.run(TOKEN)
