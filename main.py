import os
import discord
from pathlib import Path

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!loadout'):
        components = message.content.split()
        if len(components) != 3:
            await message.channel.send('Usage: !loadout [category] [gun name]')
            return

        category, gun_name = components[1], components[2]
        category_path = Path(category.lower())

        if not category_path.is_dir():
            await message.channel.send('Sorry, but the category you requested does not exist!')
            return

        loadout_file_path = category_path / 'loadout.txt'

        if not loadout_file_path.is_file():
            await message.channel.send(f"Sorry, but no loadout file found for the {category} category.")
            return

        with open(loadout_file_path, 'r') as file:
            lines = file.readlines()
            gun_loadout = [line for line in lines if gun_name.lower() in line.lower()]
            if not gun_loadout:
                await message.channel.send(f"Sorry, but the loadout for {gun_name} in {category} does not exist!")
                return

            await message.channel.send(f"Loadout for {gun_name}:\n{''.join(gun_loadout)}")

try:
    token = os.getenv("TOKEN") or ""
    if token == "":
        raise Exception("Please add your token to the Secrets pane.")
    client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e
import os
import discord
from pathlib import Path

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!loadout'):
        components = message.content.split()
        if len(components) != 3:
            await message.channel.send('Usage: !loadout [category] [gun name]')
            return

        category, gun_name = components[1], components[2]
        category_path = Path(category.lower())

        if not category_path.is_dir():
            await message.channel.send('Sorry, but the category you requested does not exist!')
            return

        loadout_file_path = category_path / 'loadout.txt'

        if not loadout_file_path.is_file():
            await message.channel.send(f"Sorry, but no loadout file found for the {category} category.")
            return

        with open(loadout_file_path, 'r') as file:
            lines = file.readlines()
            gun_loadout = [line for line in lines if gun_name.lower() in line.lower()]
            if not gun_loadout:
                await message.channel.send(f"Sorry, but the loadout for {gun_name} in {category} does not exist!")
                return

            await message.channel.send(f"Loadout for {gun_name}:\n{''.join(gun_loadout)}")

try:
    token = os.getenv("TOKEN") or ""
    if token == "":
        raise Exception("Please add your token to the Secrets pane.")
    client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e
import os
import discord
from pathlib import Path

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content == '!loadout':
        await message.channel.send('Usage: !loadout [category] [gun name]')
        
    elif message.content.startswith('!loadout '):
        components = message.content.split()
        # Assuming the components length after the command should be exactly 2
        if len(components) == 3:
            category, gun_name = components[1], components[2]
        else:
            await message.channel.send('Usage: !loadout [category] [gun name]')
            return

        category_path = Path(category.lower())
        if not category_path.is_dir():
            await message.channel.send('Sorry, but the category you requested does not exist!')
            return

        loadout_file_path = category_path / f"{gun_name.lower()}.txt"

        if not loadout_file_path.is_file():
            await message.channel.send(f"Sorry, but no loadout file found for {gun_name} in the {category} category.")
            return

        with open(loadout_file_path, 'r') as file:
            loadout_data = file.read()
            await message.channel.send(f"Loadout for {gun_name}:\n{loadout_data}")

try:
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise Exception("Discord token is not set in the environment variables.")
    client.run(token)
except Exception as e:
    print(e)
