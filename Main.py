import keep_alive
import discord
import time

TOKEN = 'OTk2NzQ2NDI5NTc1OTg3MjEw.GYeLZm.BwBWVJmNSzz2jOCBZVhtIzZGu66Kd4vFdtjpv4'
client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)
        print(f'{username}: {user_message} ({channel}')

        if message.channel.name == 'spam-pings':
            if user_message.lower() == '@everyone':
                await message.channel.send(f'@everyone')


keep_alive.keep_alive()
client.run(TOKEN)
