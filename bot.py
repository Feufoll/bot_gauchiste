# bot.py
import os
import random
import asyncio
import time

from discord.ext import commands

TOKEN = os.environ.get("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="(A)")

@bot.command(name='clivage', help="Lance une partie du jeu du clivage, syntaxe : (A)clivage *nb_de_mots* *delai* *mot_a_ajouter(optionnel)*")
async def clivage(ctx, nb_de_mots: int, delai: float, mot = 'null'):

	file = open("liste_francais.txt","r")
	words = file.readlines()
	word_set = set(words)
	file.close()
	
	
	if mot!='null':
		file = open("liste_francais.txt", "w")
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

@bot.command(name='louise-michel')
async def louise_michel(ctx):
	await ctx.send(f'Clémence-Louise Michel, dite Louise Michel Écouter, née le 29 mai 1830 à Vroncourt-la-Côte, en Haute-Marne, et morte le 9 janvier 1905 à Marseille, alias « Enjolras », est une institutrice, militante anarchiste, franc-maçonne, aux idées féministes et l’une des figures majeures de la Commune de Paris. Première à arborer le drapeau noir, elle popularise celui-ci au sein du mouvement libertaire. niCoB à aussi attribué une de ses citations à Bakou, ce qui entraîna un drama. https://fr.wikipedia.org/wiki/Louise_Michel')

bot.run(TOKEN)
