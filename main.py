import discord
from command import command
client = discord.Client()
with open("pass.txt", "r") as f:
    lines = f.readlines()
    token = lines[0]
@client.event
async def on_ready():
    print('Logged in as: {}'.format(client.user))
    await client.change_presence(activity=discord.Game(name='HE IS ALIVE!!!'))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    init = command(msg,'!')
    print('{0.author.id}: Message from {0.author}: {0.content}'.format(msg))
    if init.com() == None:
        return
    await msg.channel.send(str(init.com()))


client.run(token)