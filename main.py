import discord
import os
import tftdecks
from PIL import Image

from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

TOKEN = os.getenv('DISC_TOKEN') #Stores token in secret(.env) file

tftdecks_inst = tftdecks.TftDecks() #Creates an instance of the class TftDecks

@client.event
async def on_ready():
  print(f'{client.user} is now online!')

@client.event
async def on_message(message):
  if message.author == client.user: #prevents infinite loops with the bot
    return

  if message.content.startswith(f'!commands'): #introduction
    await message.channel.send('Hello! I am the TFT Deck Bot. Please use the !allcomps or !champs command to begin.')

  showComps = tftdecks_inst.search()
  cleanComps = "Comps: \n"
  
  for i in showComps:
    cleanComps = cleanComps + i + ', '

  cleanComps = cleanComps[:-2]
  
  if f'!allcomps' in message.content: #!allcomps command
    await message.channel.send(cleanComps)

  if message.content in showComps: #enter the name of the team comp from !allcomps command
    findPos = showComps.index(message.content)  #finds the index of the team composition of the user's input
    await message.channel.send(tftdecks_inst.findLink(findPos))

  showChamps = tftdecks_inst.champs
  cleanChamps = "Champions: \n"
  
  for i in showChamps:
    cleanChamps = cleanChamps + i + ', '

  cleanChamps = cleanChamps[:-2]
  
  if message.content.startswith(f'!champs'):
    await message.channel.send(cleanChamps)
  
  if message.content.startswith(f'!') and message.content[1:].lower() in showChamps: #enter the name of the champion from !champs command
    champ = message.content.lower()
    items = tftdecks_inst.findItems(champ)
    
    await message.channel.send(items[0])
    await message.channel.send(items[1])
    await message.channel.send(items[2])
  
client.run(TOKEN)