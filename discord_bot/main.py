from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# TODO:
# STEP 1: LOAD OUR TOKEN FROM FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 2: BOT SETUP
# We need to activate the intents for the bot to work properly
# Intents are like permissions that the bot needs to see the messages and to respond to them.
# Without intents, the bot won't be able to respond the messages
intents: Intents = Intents.default()
intents.message_content = True  # NOQA - No Quality Asurance
client: Client = Client(intents=intents)


# STEP 3: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print(f'User message is empty, ignoring.')
        return

    if is_private := user_message[0] == '?':  # question mark is going to trigger the private message functionality
        user_message = user_message[1:]  # [1:] removes the question mark from the user message

    # is_private = user_message[0] == '?'
    # if is_private:
    #     user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        # if the message is private, we send it to the user otherwise we send it back to the current channel
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# STEP 4: EVENT HANDLER FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')


# STEP 5: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)

    print(f'{channel} {username}: "{user_message}"')
    await send_message(message, user_message)


# STEP 6: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)  # pass our token which is required for bot to run


# STEP 7: RUNNING THE BOT
if __name__ == '__main__':
    main()
