import discord
import random
import youtube_dl
import asyncio
import os
import pymongo
import math
from random import choice
from pymongo import MongoClient
from youtube_dl import YoutubeDL
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
# imports library resources

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
# allows server members intent

client = commands.Bot(command_prefix = '$')
# creates an instance of `bot`
client.remove_command('help')
# removes the default help command

players = {}
# sets music player ids

player1 = ""
player2 = ""
playerBot = 802256867288023051
turn = ""
gameOver = True
# variables for tic-tac-toe

intA = 2
intB = 2
modulo = int(intA - (intB)*int(intA/intB))
split = int(intA/intB)
# variables for euclid's algorithm

board = []
# array for game board in tic-tac-toe

winConditions = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
]
# win condition array (coordinates) for tic-tac-toe

stqDict = ['All warfare is based on deception.',
  (
    'Throw your soldiers into positions whence there is no escape, and they will prefer death to flight' 
  ),
  (
    'The supreme art of war is to subdue the enemy without fighting.'
  ),
  (
    'Hence to fight and conquer in all your battles is not supreme excellence; supreme excellence consists in breaking the enemys resistance without fighting.'
  ),
  (
    'Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.'
  ),
  (
    'Strategy without tactics is the slowest route to victory. Tactics without strategy is the noise before defeat.'
  ),
  (
    'Opportunities multiply as they are seized'
  ),
  (
    'The opportunity to secure ourselves against defeat lies in our own hands, but the opportunity of defeating the enemy is provided by the enemy himself.'
  ),
  (
    'There is no instance of a nation benefitting from prolonged warfare.'
  ),
  (
    'Pretend inferiority and encourage his arrogance.'
  ),
  (
    'The good fighters of old first put themselves beyond the possibility of defeat, and then waited for an opportunity of defeating the enemy.'
  ),
  ]
# dictionary for Sun Tzu Quotes

aliceDict = [
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652111374614548/IMG_20200831_183005.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652116386545684/IMG_20200806_173845.jpg'
  ),
  ( 
   'https://cdn.discordapp.com/attachments/754550273963458580/855652156656844820/PXL_20210107_160047384.jpg' 
  ),
  (  
    'https://cdn.discordapp.com/attachments/754550273963458580/855652160288981012/IMG_20200516_174122.jpg'
  ),
  ( 
   'https://cdn.discordapp.com/attachments/754550273963458580/855652163094839306/IMG_20200529_170411.jpg' 
  ),
  (
   'https://cdn.discordapp.com/attachments/754550273963458580/855652166030065704/IMG_20200731_193226.jpg' 
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652169814638602/PXL_20210408_020724054.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652173001654312/IMG_20200921_120242_1.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652175610380306/PXL_20210513_235525956.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652176243327016/PXL_20210519_144613145.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652178287263754/PXL_20201211_022649843.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652186188808212/PXL_20210208_210008224.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652200411562004/IMG_20200418_152601_1.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652209415684116/PXL_20210611_131951501.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652218002604032/PXL_20210415_164029682.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652233293856768/IMG_20200702_192031.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652246104571954/PXL_20210510_181410188.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652248456527892/IMG_20200630_120718.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652253422845962/PXL_20210331_202402846.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652268878856222/PXL_20210510_171141783.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652272838803476/PXL_20201231_173054318.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652274789548082/PXL_20210608_202945409.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652277092220948/PXL_20210219_195317001.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652285451337728/PXL_20210420_125124332.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652296086781952/IMG_20200609_161143.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652299094229002/PXL_20210407_203045868.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652301213794314/IMG_20200527_182029.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652303260352532/IMG_20200429_101638.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652305302061096/PXL_20210424_004705409.jpg'
  ),
  (
    'https://cdn.discordapp.com/attachments/754550273963458580/855652307031425064/PXL_20210315_143303507.jpg'
  ),
  ]
# dictionary for Jacob's cat photos

lennyDict = [
  (
    '( ???? ???? ????)'
  ),
  (
    '??\_(???)_/??'
  ),
  (
    '????????????????????????'
  ),
  (
    '( ????( ???? ????( ???? ???? ????)?? ????) ????)'
  ),
  (
    '?????????????'
  ),
  (
    '(?????????????? ??)'
  ),
  (
    '(??? ???? ?????? ????)???'
  ),
  (
    '??? ??? ???_??? ??????'
  ),
  (
    '???_???'
  ),
  (
    '(?????????????????????)???'
  ),
  (
    '(????????????)???*:????????? ?????????: *???(????????????)'
  ),
  (
    '[????$????(????5????)????$????]'
  ),
  (
    '??????????????? ???? ????) ???????????????'
  ),
  (
    '( ?????????????????? )'
  ),
  (
    '(?? ???? ?? ??? ??????)'
  ),
  (
    '(??? ?? ???)'
  ),
  (
    '(?????????)'
  ),
  (
    '?????????????????? O\'RLY?'
  ),
  (
    '(????????????)???????????????'
  ),
  (
    '[????$????(???? ???? ???? ????????)????$????]'
  ),
  (
    '(????????????)???*:?????????'
  ),
  (
    '(????????????)???'
  ),
  (
    '| (??? ??????)| (???????????)'
  ),
  (
    '(????????????)'
  ),
  (
    '(?????????)'
  ),
  (
    '(???????)'
  ),
  (
    '(????????????)??? ???(????????????)'
  ),
  (
    '(?????? ?????)???'
  ),
  (
    '???(????????????)'
  ),
  (
    '????????????'
  ),
  (
    '(;????????????????`)'
  ),
  (
    '???~ ???(???)???'
  ),
  (
    '?????????'
  ),
  (
    '??? ???  ???? ???? ???? ??????'
  ),
  (
    '??? ??? ???_??? ??????'
  ),
  (
    '(??????????????????? ?????????'
  ),
  (
    '( ????? ???? ????? )'
  ),
  (
    '???(??????_???)??????'
  ),
  (
    '~(???????~)'
  ),
  (
    '???_???'
  ),
  (
    '\ (?????????) /'
  ),
  (
    '(~???????)~'
  ),
  (
    '(._.) ( l: ) ( .-. ) ( :l ) (._.)'
  ),
  (
    '??????????????????'
  ),
  (
    '??? ???????? ??? ???????? ??? ???????? ??? ???????? ??? ???????? ???'
  ),
  (
    '???????????????(???_???????????????'
  ),
  (
    '???(????????????)???'
  ),
  (
    '???(??_????)???'
  ),
  (
    '????????? ??????(`????)?????? ?????????'
  ),
  (
    '??? _ ???'
  ),
]
# dictionary for lenny faces

deadChatDict = [
  (
    'https://tenor.com/view/dead-chat-gif-18800792'
  ),
  (
    'https://tenor.com/view/googas-wet-wet-cat-dead-chat-dead-chat-xd-gif-20820186'
  ),
  (
    'https://tenor.com/view/dead-chat-dead-chat-cat-scream-gif-20859754'
  ),
  (
    'https://tenor.com/view/speed-dead-chat-fun-gif-18992739'
  ),
  (
    'https://tenor.com/view/cringe-dead-chat-kermit-wtf-gif-20484958'
  ),
  (
    'https://tenor.com/view/kel-omori-tenor-gif-20334771'
  ),
]

userDict = []
# unused dictionary for vcroulette

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('1.6 released! $doge! Being Scarlett\'s little test bitch'))
    # sets the presence for the bot
    print('Logged in as {0.user}'.format(client))
    print('_____________________________________')
    # prints in console the message when bot is turned on

@client.event
async def on_message(message):
  if message.author == client.user:
    # prevents the bot from responding to itself
    return

  #Removed. Do Not Re-Add.
    #if message.content.startswith('I\'m '):
      # runs the command if the message starts with I'm
      #await message.channel.send(f"Hi {' '.join(message.content.split()[1:])}, I\'m dad!")
      # sends message in same channel with the message content of the command message
      
    #if message.content.startswith('i\'m '):
      #await message.channel.send(f"Hi {' '.join(message.content.split()[1:])}, I\'m dad!")
      
    #if message.content.startswith('Im '):
      #await message.channel.send(f"Hi {' '.join(message.content.split()[1:])}, I\'m dad!")
      
    #if message.content.startswith('im '):
      #await message.channel.send(f"Hi {' '.join(message.content.split()[1:])}, I\'m dad!")

  if message.content.startswith('durr'):
    await message.channel.send("https://cdn.discordapp.com/attachments/854909605996920883/855188509286465536/Screenshot_20210122-161007.jpg")

  if message.content.startswith('Durr'):
    await message.channel.send("https://cdn.discordapp.com/attachments/854909605996920883/855188509286465536/Screenshot_20210122-161007.jpg")

  if message.content.startswith('hurr'):
    await message.channel.send("https://cdn.discordapp.com/attachments/754550273963458580/802339142897762324/Screenshot_20210122-161007.png")

  if message.content.startswith('Hurr'):
    await message.channel.send("https://cdn.discordapp.com/attachments/754550273963458580/802339142897762324/Screenshot_20210122-161007.png")

  if message.content.startswith('red sus'):
    await message.channel.send("https://tenor.com/view/among-us-red-sus-suspect-among-gif-19597730")

  if message.content.startswith('Red sus'):
    await message.channel.send("https://tenor.com/view/among-us-red-sus-suspect-among-gif-19597730")

  if message.content.startswith('When the impostor is sus'):
    await message.channel.send("https://tenor.com/view/among-us-red-sus-suspect-among-gif-19597730")

  if message.content.startswith('when the impostor is sus'):
    await message.channel.send("https://tenor.com/view/among-us-red-sus-suspect-among-gif-19597730")

  #if message.content.startswith('Sus'):
    # await message.channel.send("https://tenor.com/view/among-us-red-sus-suspect-among-gif-19597730")

  #if message.content.startswith('sus'):
    # await message.channel.send("https://tenor.com/view/among-us-red-sus-suspect-among-gif-19597730")

  if message.content.startswith("pog"):
    await message.channel.send("https://cdn.discordapp.com/attachments/745438682902954104/804446434257534986/video0_3.mp4")

  if message.content.startswith("Pog"):
    await message.channel.send("https://cdn.discordapp.com/attachments/745438682902954104/804446434257534986/video0_3.mp4")

  if message.content.startswith("Paedophile"):
    await message.channel.send("https://tenor.com/view/uno-card-reverse-gif-15490757")

  if message.content.startswith("paedophile"):
    await message.channel.send("https://tenor.com/view/uno-card-reverse-gif-15490757")

  if message.content.startswith("Pedophile"):
    await message.channel.send("https://tenor.com/view/uno-card-reverse-gif-15490757")

  if message.content.startswith("pedophile"):
    await message.channel.send("https://tenor.com/view/uno-card-reverse-gif-15490757")

  if message.content.startswith("Sussy"):
    await message.channel.send("https://cdn.discordapp.com/attachments/750503879254343812/855165242908737576/Thats_a_bit_sussy.mp4")

  if message.content.startswith("sussy"):
    await message.channel.send("https://cdn.discordapp.com/attachments/750503879254343812/855165242908737576/Thats_a_bit_sussy.mp4")

  if message.content.startswith("Ya\'ll"):
    await message.channel.send("Remember kids, it\'s y\'all! Ya\'ll is the sign of the devil!")

  if message.content.startswith("ya\'ll"):
    await message.channel.send("Remember kids, it\'s y\'all! Ya\'ll is the sign of the devil!")

  if message.content.startswith("korea"):
    await message.channel.send("Korea? I love Korea! Korea is the greatest country on Earth and has no downsides whatsoever! Annyeong hasao nan Maya! NO! I AM NOT A KOREABOO! I'm basically just a Korean born in the wrong country :pensive: Saranghae Bangtan Sonyaedon!! Do you want to go to Korea? I'm going to school in Korea!")

  if message.content.startswith("Korea"):
    await message.channel.send("Korea? I love Korea! Korea is the greatest country on Earth and has no downsides whatsoever! Annyeong hasao nan Maya! NO! I AM NOT A KOREABOO! I'm basically just a Korean born in the wrong country :pensive: Saranghae Bangtan Sonyaedon!! Do you want to go to Korea? I'm going to school in Korea!")
  await client.process_commands(message)

@client.command()
async def testrole(ctx, member : discord.Member, role : discord.Role):
    await member.add_roles("test role 1")

# chat commands -------------------------------------------
@client.command()
async def stq(ctx):
  response = random.choice(stqDict)
  # runs the command if the message starts with $stq
  await ctx.send(response)
  # sends value of 'response' when triggered

@client.command()
async def alice(ctx):
  response = random.choice(aliceDict)
  await ctx.send(response)

@client.command()
async def vttoxic(ctx):
  await ctx.send("https://twitch.tv/vttoxicsamurai")
  # 6/17/21: I'm disabled and forgot ctx.send existed

@client.command()
async def call(ctx):
  await ctx.send("@here")

@client.command()
async def adam(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/754550273963458580/804441000658468864/2Q.png")

@client.command()
async def phys(ctx):
  await ctx.send("https://arxiv.org/")

@client.command()
async def navyseals(ctx):
  await ctx.send("What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little \"clever\" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.")

@client.command()
async def rejoin(ctx):
  await ctx.send("https://discord.gg/4TZE3SWFMw")

@client.command()
async def rejoinbtp(ctx):
  await ctx.send("https://discord.gg/UXZqCguJK6")

@client.command()
async def rejoines(ctx):
  await ctx.send("https://discord.gg/gAnKjFqgWZ")

@client.command()
async def apiref(ctx):
  await ctx.send("https://discordpy.readthedocs.io/en/stable/api.html")

@client.command()
async def help(ctx):
  await ctx.send("```\nCommands:\n$stq - Sun Tzu Quotes\n$twitch - Twitch link\n$call - @ here\n$phys - Scientific papers link\n$navyseals - Navy Seals Copypasta\n$adam - Adam Wilson\n$vcroulette - Coming soon\n$rejoin/$rejoinbtp - Discord invite link\n$APIref - Documentation\n$join/leave - Lets the bot join/leave your current vc\n$vcHelp - Displays help for voice channel commands\n$tttHelp - Displays help for tic tac toe commands\n$alice - Pictures of Jacob's cat\n$clips - Clips channel link\n$lenny - Posts a random lenny face\n$sources - Links to sources I used to create this bot\n$useless - This command is useless, do not use it.\n$doge - Posts a doge, however there's a chance for a rare or ultra rare doge\n$report - Discord report link\n$rng (number) - Chooses a random number between 1 and the entered number\n$deadchat - Calls @ here and dead chats\n$github - github link\nPrefixes:\nHurr/Durr - Hurrguy/Durrguy\nRed sus - red sus before\nWhen the imposter is sus - sus!\nI'm - Dad joke\nPog - WOO BABY\nP(a)edophile - Uno reverse\nYa\'ll - Corrects your ignorant mistake\nSussy - sussus amogus\nKorea - Korea spam```")

@client.command()
async def clips(ctx):
  await ctx.send("https://www.youtube.com/channel/UCBPqyaDCISZlXQXOZJbEPCw")

@client.command()
async def updateBot(ctx):
  await ctx.send("Bot updated to 1.6.11!")

@client.command()
async def changelog(ctx):
  await ctx.send("# 1.6.11: created $github, edited $help (8/2/21)")

@client.command()
async def useless(ctx, amount=1):
  await ctx.channel.purge(limit=amount)
  await ctx.send("This command is useless, stop using it.", delete_after=3)

@client.command()
async def lenny(ctx):
  response = random.choice(lennyDict)
  await ctx.send(response)

@client.command()
async def sources(ctx):
  await ctx.send('Bot sources:\ndiscord.py discord\nhttps://discordpy.readthedocs.io/en/stable/api.html\nhttps://stackoverflow.com/questions/65891543/how-would-i-respond-to-a-message-with-what-the-user-said\nhttps://github.com/discordjs/discord.js/issues/439\nhttps://realpython.com/how-to-make-a-discord-bot-python/\nhttps://stackoverflow.com/questions/49076798/discord-py-add-role-to-someone\nhttps://stackoverflow.com/questions/49286640/how-to-set-bots-status\nhttps://stackoverflow.com/questions/63493179/nameerror-name-bot-is-not-defined\nhttps://www.youtube.com/channel/UCR-zOCvDCayyYy1flR5qaAg\nhttps://www.youtube.com/watch?v=K5pkOrjeAIs\nhttps://www.youtube.com/channel/UCwBjRPUuOefh6iFvG6zLhrg\nhttps://www.youtube.com/watch?v=pL2EuhSV7tw\nhttps://www.youtube.com/channel/UCdNnHNkhaRYr-3nhQqY7_dw\nhttps://www.youtube.com/watch?v=ml-5tXRmmFk\nhttps://www.youtube.com/watch?v=wBbgCUQZNzM\nhttps://stackoverflow.com/questions/22786068/how-to-avoid-http-error-429-too-many-requests-python')

@client.command()
async def report(ctx):
  await ctx.send("https://dis.gd/report")

@client.command()
async def rng(ctx, inputNum : int):
  num = random.randint(1, inputNum)
  await ctx.send(f"{num}")
# 7/7/21: All my own code!

@rng.error
async def rng_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please mention a number!")
# 7/7/21: This one too

@client.command()
async def deadchat(ctx):
  response = random.choice(deadChatDict)
  await ctx.send("dead chat xd ||@here||")
  await ctx.send(response)

@client.command()
async def github(ctx):
  await ctx.send("https://github.com/ToxicSamurai")

# vc commands----------------------------------------------
@client.command()
async def join(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    await ctx.send("Joined the voice channel!")
  else:
    await ctx.send("You\'re not in a voice channel!")
# join vc command

@client.command()
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("Left the voice channel!")
  else:
    await ctx.send("I\'m not in a voice channel!")
# leave vc command

@client.command()
async def play(ctx, url : str):
  song_there = os.path.isfile("song.mp3")
  try:
      if song_there:
        os.remove("song.mp3")
  except PermissionError:
    await ctx.send("Wait! There\'s already a song playing!")
    return
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General') 
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

  ydl_opts = {
  'format': 'bestaudio/best',
  'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192',
    }]
  }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  for file in os.listdir("./"):
    if file.endswith(".mp3"):
      os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
# plays a link
# 6/16/21: I spent 6 fucking hours trying to figure out why it didn't work because it said it was already connected
# 6/16/21: It was because I did fucking $join before $play god fucking damnit

@client.command()
async def skipto(ctx, url : str):
  await ctx.send("Skipping song!")
  await ctx.guild.voice_client.disconnect()
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  song_there = os.path.isfile("song.mp3")
  try:
      if song_there:
        os.remove("song.mp3")
  except PermissionError:
    await ctx.send("Wait! There\'s already a song playing!")
    return
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General') 
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

  ydl_opts = {
  'format': 'bestaudio/best',
  'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192',
    }]
  }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  for file in os.listdir("./"):
    if file.endswith(".mp3"):
      os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
# skips the song by leaving, rejoining, and playing song
# 6/17/21: HOLY FUCKING SHIT IT WORKED THE FIRST TRY
# 6/18/21: Doesn't work on Heroku perma build -.-
# 6/18/21: Works on Heroku perma build, FFmpeg wasn't installed on Heroku lulw
# 6/22/21: Playlists like half work, it'll play the first song and occasionally the second upon next url req
# 6/22/21: Rewrite imminent. Fuck.

@client.command()
async def stop(ctx):
  await ctx.send("Stopping all songs!")
  await ctx.guild.voice_client.disconnect()
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
# stops song by leaving and rejoining 
# play audio commands

@client.command()
async def vcHelp(ctx):
  await ctx.send("```\nThis bot can play audio from a link! Use these commands:\n$play url - Plays audio from the url\n$skipto url - Skips current song and plays audio from the url\n$stop - Stops music```")

# tic-tac-toe commands----------------------------------------------
@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
  global count
  global player1
  global player2
  global playerBot 
  global turn
  global gameOver

  if gameOver:
    global board
    board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
             ":white_large_square:", ":white_large_square:", ":white_large_square:",
             ":white_large_square:", ":white_large_square:", ":white_large_square:"]
    turn = ""
    gameOver = False
    count = 0

    player1 = p1
    player2 = p2

    line = ""
    for x in range(len(board)):
      if x == 2 or x == 5 or x == 8:
        line += " " + board[x]
        await ctx.send(line)
        line = ""
      else:
        line += " " + board[x]
    # prints the board
  
  if str(player1.id) == str(player2.id):
    gameOver = True
    await ctx.send("Mention a different player other than yourself!")
    # prevents a player playing with themselves
    # 6/23/21: Worked the first time lmao, just needs some refining. I made this segment entirely myself and I'm proud as fuck
  #elif str(player1.id) == str(playerBot.id):
    #gameOver = True
    #await ctx.send("Mention a different player other than the bot!")
  #elif str(player2.id) == str(playerBot.id):
    #gameOver = True
    #await ctx.send("Mention a different player other than the bot!")
    # prevents a player playing with the bot
    # 6/24/21: doesn't work, needs to be fixed or replaced with the bot playing
  elif str(player1.id) != str(player2.id):
    num = random.randint(1, 2)
    if num == 1:
      turn = player1
      await ctx.send("It's <@" + str(player1.id) + ">'s turn!")
    elif num == 2:
      turn = player2
      await ctx.send("It's <@" + str(player2.id) + ">'s turn!")
    # determines the turn order
  else:
    await ctx.send("A game is already in progress!")
# initializes game
# 6/23/21: Worked like the fourth time lmao

@client.command()
async def place(ctx, pos : int):
  global turn
  global player1
  global player2
  global playerBot
  global board
  global count

  if not gameOver:
    mark = ""
    if turn == ctx.author:
      if turn == player1:
        mark = ":regional_indicator_x:"
      elif turn == player2:
        mark = ":o2:"
      if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
        board[pos - 1] = mark
        count += 1

        line = ""
        for x in range(len(board)):
          if x == 2 or x == 5 or x == 8:
            line += " " + board[x]
            await ctx.send(line)
            line = ""
          else:
            line += " " + board[x]
          # prints board again

        checkWinner(winConditions, mark)
        if gameOver:
          await ctx.send(mark + " wins!")
        elif count >= 9:
          await ctx.send("Tie!")

        if turn == player1:
          turn = player2
        elif turn == player2:
          turn = player1
        # alternates turns

      else:
        await ctx.send("Your number must be between 1 and 9 and be on an unmarked tile!")
    else:
      await ctx.send("It is not your turn!")
  else:
    await ctx.send("Please start a new game!")
# place tile command

def checkWinner(winConditions, mark):
  global gameOver
  for condition in winConditions:
    if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
      gameOver = True
# checks to see if anyone has won

@client.command()
async def endgame(ctx):
  global gameOver
  if not gameOver:
    gameOver = True
    await ctx.send("Current game cancelled!")
  else:
    await ctx.send("There's no game currently running!")

@tictactoe.error
async def tictactoe_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please mention 2 players!")
  elif isinstance(error, commands.BadArgument):
    await ctx.send("Please make sure to mention players!")
# error handler for tic tac toe initilization

@place.error
async def place_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please enter a position!")
  elif isinstance(error, commands.BadArgument):
     ctx.send("Please enter a number!")
# error handler for tic tac toe command

@client.command()
async def tttHelp(ctx):
  await ctx.send("```This bot allows two different players to play tic tac toe over Discord! Use these commands:\n$tictactoe @player1 @player2 - Creates a tic tac toe game between two pinged players\n$place number  - Places an X or O on a tile (must be in a game and number must be between 1 and 9)\n$endgame - Ends the current game\nIt's currently not available to play with the bot\nThe turn order is determined randomly.```")
  
# doge commands----------------------------------------------
@client.command()
async def doge(ctx):
  num = random.randint(1, 1000)
  if num >= 1 and num <= 1000 and num != 10 and num != 20 and num != 30 and num != 40 and num != 110 and num != 120 and num != 130 and num != 140 and num != 210 and num != 220 and num != 230 and num != 240 and num != 310 and num != 320 and num !=330 and num != 333 and num != 340 and num !=410 and num != 420 and num != 430 and num != 440 and num != 510 and num != 520 and num != 530 and num !=540 and num != 610 and num != 620 and num !=630 and num != 640 and num != 666 and num != 710 and num != 720 and num != 730 and num != 740 and num != 810 and num != 820 and num != 830 and num != 840 and num != 910 and num != 920 and num != 930 and num != 940:
    await ctx.send("Common doge!")
    await ctx.send("https://cdn.discordapp.com/attachments/802258582950117430/857745875555975178/5845e770fb0b0755fa99d7f4.png")
  # normal doge command
  elif num == 10 or num == 110 or num == 210 or num == 310 or num == 410 or num == 510 or num == 610 or num == 710 or num == 810 or num == 910:
    await ctx.send("Rare angry doge! **1/100 chance!**")
    await ctx.send("https://cdn.discordapp.com/attachments/802258582950117430/857732280151703552/k5WRHNIjkJomYQXE5Y-X0H5wMe58lSUOD7E0n0DbwKYAnqS7GKbo28eWf38cOwvGEkcV4gxL4Ru6cDbYqUgCE1e5CAqLhPJ3m0NM.png")
  elif num == 20 or num == 120 or num == 220 or num == 320 or num == 420 or num == 520 or num == 620 or num == 720 or num == 820 or num == 920:
    await ctx.send("Rare femboy doge! **1/100 chance!**")
    await ctx.send("https://cdn.discordapp.com/attachments/802258582950117430/857734252065980437/Doge-Head-Transparent-Background.png")
  elif num == 30 or num == 130 or num == 230 or num == 330 or num == 430 or num == 530 or num == 630 or num == 730 or num == 830 or num == 930:
    await ctx.send("Rare chubby doge! **1/100 chance!**")
    await ctx.send("https://cdn.discordapp.com/attachments/802258582950117430/857732080031760384/0HVTKtSGhO5lzZ7te5ZRtt1H-cOKK24VcBph0nMu5o38OV7Olr9b0r3KERJadmRrbkvUgAjs9sFnqmbxNexBR0e7iF4-JZqS8_Xj.png")
  elif num == 40 or num == 140 or num == 240 or num == 340 or num == 440 or num == 540 or num == 640 or num == 740 or num == 840 or num == 940:
    await ctx.send("Rare chad doge! **1/100 chance!**")
    await ctx.send("https://cdn.discordapp.com/attachments/802258582950117430/857733627222425620/3cqykx.png")
  # rare doge commands
  elif num == 333:
    await ctx.send("Rare edible doge! **1/1000 chance!**")
    await ctx.send("https://cdn.discordapp.com/attachments/802258582950117430/857732866637037628/5845e687fb0b0755fa99d7ee.png")
  elif num == 666:
    await ctx.send("Rare ghost doge! **1/1000 chance!**")
    await ctx.send("https://cdn.discordapp.com/attachments/802258582950117430/857732965365579812/5845e643fb0b0755fa99d7ea.png")
  # ultra rare doge commands

# vcroulette commands----------------------------------------------
#@client.command()
#async def vcroulette(ctx, member : str):
#  num = random.randint(1, 1000)

@client.command()
async def moveTest(ctx, member: discord.Member):
  await member.move_to(channel=864264378362494978)

#@moveTest.error
#async def moveTest_error(ctx):
  #if isinstance(error, commands.MissingRequiredArgument):
    #await ctx.send("worker.1 reports: commands.MissingRequiredArgument!")
  #elif isinstance(error, commands.BadArgument):
    #await ctx.send("worker.1 reports: commands.BadArgument!")
  #elif isinstance(error, commands.CommandInvokeError):
    #await ctx.send("worker.1 reports: commands.CommandInvokeError!")
# unused error handler for moveTest as of 7/13/21

# euclid's algorithm commands----------------------------------------------
@client.command()
async def euclid(ctx, p : int, q : int):
  global intA
  global intB
  global modulo
  global split

  intA = p
  intB = q

  while modulo != 0:
    intA = intB
    intB = modulo
    split = int(intA/intB)
    modulo = intA - (intB * split)

    ctx.send(intB)

# suggestion commands----------------------------------------------
@client.command()
async def suggest(ctx, suggestion : str):
  user = client.get_user(253668275496419329)
  await user.send("This is a test message.")
  ctx.send("Thanks for the suggestion!")
# 7/12/21: Mostly my own code, but still doesn't work with an error I don't know
# unused as of 7/12/21

# database commands----------------------------------------------
@client.command()
async def pingTest(ctx):
  mongo_url = "mongodb+srv://ToxicSamurai:nQdQURG6PXm6Qyx@epicgamerbotdb.qqcgu.mongodb.net/EpicGamerBotDB?retryWrites=true&w=majority"
  cluster = MongoClient(mongo_url)
  db = cluster["EpicGamerBotDB"]
  collection = db["EconomyBank"]
  # initilizes MongoDB

  pingTest_cm = {"command":1}
  collection.insert_one(pingTest_cm)

  await ctx.channel.send("Ping sent to database")
# unused as of 7/7/21

#@client.command()
#async def message_count(ctx, channel: discord.TextChannel=None):
  #channel = channel or ctx.channel
  #count = 0
  #async for _ in channel.history(limit=None):
    #count += 1
  #await ctx.send("There were {} messages in {}".format(count, channel.mention))
# https://stackoverflow.com/questions/52214425/how-to-get-how-many-messages-has-been-sent-in-a-channel

client.run('ODAyMjU2ODY3Mjg4MDIzMDUx.YAsl7g.J3IxXmHg_XICdddBjeOriJ6kGlY')

#steps to push to Heroku
# Go to save repo
# Type cmd into location bar
#  "heroku login"
#  Enter
#  "git commit -am "word""
#  "git add ."
#  "git push heroku master" (could be main instead of master)

#steps to create a new requirements.txt
# Go to save repo
# Type cmd into location bar
# "pip freeze > requirements.txt"

#steps to clear build cache
# Go to save repo
# Type cmd into location bar
# "heroku builds:cache:purge -a epic-gamer-music-bot"
# "epic-gamer-music-bot"

#changelog
# updated $updateBot and $changelog should be assumed
# retroactive 1.0: stq update, 1.1, prefix update, 1.2 command update, 1.3 vc update, 1.4 alice update
# 1.4.7: created $clips, edited $help
# 1.4.8: created $vcHelp, created and removed an HTTP Error 429 override, $updated $help, edited $help
# 1.4.9: updated stq dictionary, updated $vcHelp, 1.5 code implemented but unused
# 1.4.10: testing for 1.5 has begun, created $changelog
# 1.4.11: fixed many errors in 1.5 update, updated $changelog
# 1.5.0: created $tictactoe and $place (allows 2 players to play tictactoe), created non-asynchronous command checkWinner to check win conditions in a game, created error handlers for tic tac toe (tictactoe_error and place_error), updated $help, created $tttHelp
# 1.5.1: created $endgame, updated $tttHelp
# 1.5.2: edited $tictactoe to prevent playing with one player (484, 3), updated $tttHelp
# 1.5.3: edited $tictactoe so the one player countermeasure is determined before the player who starts is determined, updated $tttHelp
# 1.5.4: edited $tictactoe to make 1.5.3 work, edited $tttHelp
# 1.5.5: created $useless, edited $help
# 1.5.5.1: updated $useless, created $lenny, created lenny dictionary, edited $help
# 1.5.5.2: updated $tictactoe to prevent playing with the bot and breaking the game and some spelling errors, updated $tttHelp
# 1.5.5.3: 1.5.5.3: created $sources, edited $help, disabled tictactoe countermeasures 2 and 3
# 1.5.5.4: edited $help, code for 1.6 begun
# 1.6: created $doge (posts an img of doge, can be rare), updated $help, mentally preparing for the vc commands rewrite
# 1.6.1: created korea as a prefix, edited $help
# 1.6.2: edited on_message.im/Im/i\'m/I\'m to prevent responding to words that begin with im-
# 1.6.3: removed $breakMe
# 1.6.4: created $report
# 1.6.5: created $dmTest, updated $help
# 1.6.6: created $rng, updated $help
# 1.6.7: created error handler for $rng (@rng.error() - rngErrorHandler)
# 1.6.8: fixed and edited error handler for $rng (@rng.error - rng_error) (7/7/21)
# 1.6.9: allowed server members intent, updated $sources (7/12/21)
# 1.6.10: (updated changelog) reorganized indentation on stqDict, created $deadchat, created dict for $deadchat (deadChatDict), updated $help, deleted song.mp3 from local (7/15/21)
# 1.6.11: created $github, edited $help (8/2/21)
# 1.x: created $euclid and variables
# 1.x: created $vcroullete and error handler (@vcroulette.error - vcroulette_error), updated $help, updated $souces
# 1.x: created $suggest and error handler (@suggest.error - suggest_error), updated $help

#sources: 
# discord.py discord
# https://discordpy.readthedocs.io/en/stable/api.html
  # https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-send-a-dm
# https://stackoverflow.com/questions/65891543/how-would-i-respond-to-a-message-with-what-the-user-said
# https://github.com/discordjs/discord.js/issues/439 
# https://realpython.com/how-to-make-a-discord-bot-python/
# https://stackoverflow.com/questions/49076798/discord-py-add-role-to-someone
# https://stackoverflow.com/questions/49286640/how-to-set-bots-status
# https://stackoverflow.com/questions/63493179/nameerror-name-bot-is-not-defined
# https://www.youtube.com/channel/UCR-zOCvDCayyYy1flR5qaAg
  # https://www.youtube.com/watch?v=K5pkOrjeAIs
# https://www.youtube.com/channel/UCwBjRPUuOefh6iFvG6zLhrg
  # https://www.youtube.com/watch?v=pL2EuhSV7tw
# https://www.youtube.com/channel/UCdNnHNkhaRYr-3nhQqY7_dw
  # https://www.youtube.com/watch?v=ml-5tXRmmFk
  # https://www.youtube.com/watch?v=wBbgCUQZNzM
# https://stackoverflow.com/questions/22786068/how-to-avoid-http-error-429-too-many-requests-python
# https://www.youtube.com/channel/UC2ITRZ4_Di-KMHSIylTQbBA
  # https://www.youtube.com/watch?v=HPaadO_sRD4
# https://docs.python.org/3/library/random.html
# https://www.youtube.com/channel/UCPzRFFn1B_-ztBy5ZTNnP1A
  # https://www.youtube.com/watch?v=TaQq9Il5ifQ
# https://www.semicolonworld.com/question/62321/move-all-members-in-a-channel-to-another-with-discord-py
# https://stackoverflow.com/questions/55149372/discord-py-tag-a-random-user/55150213
# https://en.wikipedia.org/wiki/Euclidean_algorithm
# https://stackoverflow.com/questions/21608593/euclidean-algorithm-gcd-in-python
