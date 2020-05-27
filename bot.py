# bot.py
import os
import random
import asyncio
import time
import psycopg2

from discord.ext import commands
from boto.s3.connection import S3Connection

TOKEN = os.environ.get("DISCORD_TOKEN")
DATABASE_URL = os.environ['DATABASE_URL']

bot = commands.Bot(command_prefix="(A)")

@bot.command(name='clivage', help="Lance une partie du jeu du clivage, syntaxe : (A)clivage *nb_de_mots* *delai* *mot_a_ajouter(optionnel)*")
async def clivage(ctx, nb_de_mots: int, delai: float, mot = 'null'):

	file = open("liste_francais.txt","r",encoding = "ISO-8859-15")
	words = file.readlines()
	word_set = set(words)
	file.close()
	
	
	if mot!='null':
		file = open("liste_francais.txt", "w", encoding = "ISO-8859-15")
		word_set.add(mot)
		file.seek(0)
		file.writelines(list(word_set))
		file.close()
		message = await ctx.send(mot)
		await message.add_reaction('🇬')
		await message.add_reaction('🇩')
		await asyncio.sleep(delai)
		
	
	for _ in range(nb_de_mots):
		response = random.choice(words)
		message = await ctx.send(response)
		await message.add_reaction('🇬')
		await message.add_reaction('🇩')
		await asyncio.sleep(delai)

	

	
@bot.command(name='barcelone36')
async def barcelone36(ctx):
	await ctx.send(f'La révolution sociale espagnole de 1936 (revolución social española de 1936), couramment désignée sous le nom de révolution espagnole (revolución española)1, englobe tous les événements de type révolutionnaire déclenchés en Espagne, durant la guerre civile, en réponse à la tentative de coup d\'État militaire les 17 et 18 juillet 1936. Les principaux représentants de ces mouvements étaient la Confédération nationale du travail (CNT/AIT), la Fédération anarchiste ibérique (FAI), le Parti ouvrier d\'unification marxiste (POUM), ainsi que les ailes radicales du Parti socialiste ouvrier espagnol (PSOE) et de l\'Union générale des travailleurs (UGT). Les bases idéologiques de cette révolution se rattachent très clairement à l\'anarcho-syndicalisme et au communisme libertaire, extrêmement puissant en Espagne dans les années 1930, mais aussi en partie au marxisme révolutionnaire. https://fr.wikipedia.org/wiki/R%C3%A9volution_sociale_espagnole_de_1936')


bot.run(TOKEN)
