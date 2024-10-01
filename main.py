from telethon.sync import TelegramClient, events
import logging


api_id = '21638466'
api_hash = 'bb4f4118aba1864c3a64391315d37464'
bot_token = '6664976186:AAFW6_6IhzWZqfBuk7IRo1WSi-GDN8oJjuA'
source_channel_id = -1001955364788  # Replace with the source channel ID
groups = [
    {'name': 'group_1', 'values': [-1001918773030, -1001977156216]},
    {'name': 'group_2', 'values': [-1002273611599, -1002341478825]},
    {'name': 'all', 'values': [-1001918773030, -1001977156216, -1002273611599, -1002341478825]}
]

destination_channel_ids = []  # Replace with the correct channel IDs (-100 prefix for channels)


#destination_channels
# 1_dest : -1001918773030
# 2_dest : -1001977156216
# 3_dest : -1002273611599
# 4_dest : -1002341478825




client = TelegramClient('message_forwarder_bot', api_id, api_hash)

client.start(bot_token=bot_token)


@client.on(events.NewMessage(chats=source_channel_id))
async def forward_message(event):
    try:
        # Extract text from the message and send it as a new message
        message = event.message
        text_of_message = message.message

        if len(message.message) != 0:
            print(f"\nMessage: '{message.message}' ")
        else:
            print(f"\t\t\tSome media(empty message text)\n")
        print(f"Forwarded message to : ")

        groups_names = text_of_message[0:7]

        if groups_names[0:3] == 'all':
            for group in groups:
                if group['name'] == 'all':
                    destination_channel_ids = group['values']
                    text_of_message = text_of_message[3:]
                    
        elif groups_names[0:5] == 'group':
            for group in groups:
                if group['name'] == groups_names:
                    destination_channel_ids = group['values']
                    text_of_message = text_of_message[7:]
                    
        
        message.message = text_of_message
        for destination_channel_id in destination_channel_ids:
            await client.send_message(destination_channel_id, message)
            print(f"\t\t\t{destination_channel_id}")
        
    except Exception as e:
        print(f"Failed to forward message: {str(e)}")
        

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Usage example
logging.info('Bot started successfully!')

client.run_until_disconnected()