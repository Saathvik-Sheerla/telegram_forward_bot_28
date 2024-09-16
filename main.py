from telethon.sync import TelegramClient, events
import logging


api_id = '21638466'
api_hash = 'bb4f4118aba1864c3a64391315d37464'
bot_token = '6664976186:AAFW6_6IhzWZqfBuk7IRo1WSi-GDN8oJjuA'
source_channel_id = -1001955364788  # Replace with the source channel ID
destination_channel_ids = [-1001918773030, -1001977156216]  # Replace with the correct channel IDs (-100 prefix for channels)


# 1673550274 , <--Destchannel IDS
# 4061917094
# 1918773030


client = TelegramClient('message_forwarder_bot', api_id, api_hash)

client.start(bot_token=bot_token)


@client.on(events.NewMessage(chats=source_channel_id))
async def forward_message(event):
    try:
        flag = True
        print(f"Forwarded message to : \n")
        for destination_channel_id in destination_channel_ids:
            # Extract text from the message and send it as a new message
            message = event.message
            await client.send_message(destination_channel_id, message)
            if flag == True:
                if len(message.message) != 0:
                    print(f"\t\t\tMessage: {message.message}\n")
                else:
                    print(f"\t\t\tSome media(empty message text)\n")
                flag = not flag
            print(f"\t\t\t{destination_channel_id}")
            
    except Exception as e:
        print(f"Failed to forward message: {str(e)}")
        

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Usage example
logging.info('Bot started successfully!')

client.run_until_disconnected()
