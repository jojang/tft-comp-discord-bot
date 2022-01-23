import discord
import os
import tftdecks

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

  if message.content.startswith(f'!hello'): #introduction
    await message.channel.send('Hello! I am the TFT Deck Bot. Please use the !allcomps command to view the list of the most used team compositions at the moment. Enter a team composition from the list to receive a link to its guide.')

  showComps = tftdecks_inst.search()

  if f'!allcomps' in message.content: #!allcomps command
    await message.channel.send(showComps)

  if str(message.content) in showComps: #enter the name of the team comp from !allcomps command
    findPos = showComps.index(message.content)  #finds the index of the team composition of the user's input
    await message.channel.send(tftdecks_inst.findLink(findPos)) 
  
client.run(TOKEN)