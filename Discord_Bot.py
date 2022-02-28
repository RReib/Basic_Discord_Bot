import discord 
import random
import time

#Bot token goes here, it can be generated from the discord developer site.
TOKEN = 'OTQ1NzM0NjQyMjEwODYxMTI2.YhUeBQ.1m9HAGwirm1XqvK9PQGFTYIbdAs'

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'dark':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'goodnight':
            await message.channel.send(f'have a good night {username}. See you next time.')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!roll_d20':
            response = f'The D20 landed on: {random.randrange(20)}'
            await message.channel.send(response)
            return

    if message.channel.name == 'light':
        if user_message.lower() == 'im back':
            await message.channel.send(f'Welcome back {username}, its good to see you again.')
            return
        elif user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}.')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
        elif user_message.lower() == '!rd20':
            response = f'The D20 landed on: {random.randrange(20)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!rd6':
            response = f'The D6 landed on: {random.randrange(6)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!r2d6':
            response = f'The first D6 landed on {random.randrange(6)} and the second on {random.randrange(6)}'
            await message.channel.send(response)
            return

    if user_message.lower() == '!announcements':
        await message.channel.send('There is currently [1] announcement in the string.')
        time.sleep(2)
        await message.channel.send('Try !view to see announcements.')

    if user_message.lower() == '!sentience?':
        await message.channel.send('As of 2/22/22 the light server bot will be intermitintly live. The command list is currently small and will be updated soon.')
        return
        
    if user_message.lower() == '!music':
        music = ['https://music.youtube.com/playlist?list=OLAK5uy_l63UotXvycgKWYn_GkpJcyRfMEf78qYxg']
        await message.channel.send(random.choice(music))
        return

    if user_message.lower() == '!view':
        await message.channel.send('As of 2/22/22 the light server bot will be intermitintly live. The command list is currently small and will be updated soon.')
        return

    if user_message.lower() == '!help':
        await message.channel.send('!rd6 \n!r2d6 \n!rd20 \n!sentience? \n!music \n!announcements')
        return

client.run(TOKEN)