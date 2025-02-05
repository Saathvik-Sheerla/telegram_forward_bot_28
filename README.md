##Telegram_Forward_bot:

#What it does:  
Forwards messages/media from one channel(source) to multiple channels(destination).

#How it does: 
Uses Telegram API , telethon library and a bot to listen for new messages in source channel and an event is fired to forward messages to destination channels (loop for multiple channels).

#Use case: 
In an organisation to send a message that "there is a holiday tomorrow"/"there is a meeting at __ " , the head of the organisation will have to manually forward the message to multiple departments channels sometimes there may be 100 200 or more destination channels and with this project it’s just one message to source channel and bot will forward the message to all destination channels within milliseconds.
