import discord
import os
import requests
import json
import random
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

sad_words = [
  'crying', 'depressed', 
  'sad', 'angry', 'miserable', 
  'depression', 'unhappy', 'pain'
]

encouragements = [
  "I love you, it's going to be ok",
  "Don't say that! Be happy",
  "Cheer up!",
  "You're going to be ok :)",
  "Things will get better"
]

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  
  if message.author == client.user:
    return
  
  if message.content.startswith('!hello'):
    await message.channel.send("Hello!")
  
  if message.content.startswith('!inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if any(word in message.content for word in sad_words):
    await message.channel.send(random.choice(encouragements))


client.run(os.environ['TOKEN'])