from telethon import TelegramClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Telegram Client
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client = TelegramClient('session_name', api_id, api_hash)

# Define channels to scrape
channels = ['channel1', 'channel2', 'channel3', 'channel4', 'channel5']


async def fetch_messages():
    all_messages = []

    # Connect to the Telegram client
    await client.start()

    # Loop through the channels
    for channel in channels:
        try:
            # Get the messages from the channel
            messages = await client.get_messages(channel, limit=100)  # Adjust limit as needed
            for message in messages:
                all_messages.append({
                    'sender': message.sender_id,
                    'timestamp': message.date,
                    'content': message.text,
                    'channel': channel,
                    'media': message.media if message.media else None
                })
        except Exception as e:
            print(f"Error fetching from {channel}: {e}")

    # Close the client after fetching messages
    await client.disconnect()

    return all_messages
