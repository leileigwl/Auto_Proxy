from telethon import TelegramClient, events
from tel import config
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

api_id = config.api_id
api_hash = config.api_hash
user_id = config.user_id
client = TelegramClient('tel/anon.session', api_id, api_hash)


class Tel_Proxy():
    def __init__(self):
        pass

    async def main(self):
        await client.send_message(user_id, '/help')

        @client.on(events.NewMessage(from_users=user_id))
        async def handler(event):
            with open('session.txt', 'w', encoding='utf8') as f:
                f.write(event.message.text)
            await client.disconnect()

        await client.run_until_disconnected()

    async def get(self):
        client.loop.run_until_complete(self.main())
