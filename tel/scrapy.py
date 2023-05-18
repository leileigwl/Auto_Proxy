from telethon import TelegramClient, events
from tel import config
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


class Tel_Proxy():
    def __init__(self):
        self.api_id = config.api_id
        self.api_hash = config.api_hash
        self.user_id = config.user_id
        self.client = TelegramClient('anon', self.api_id, self.api_hash)
        self.client.connect_timeout = 3.0
        self.client.connect_retries = 2

    async def main(self):
        await self.client.send_message(self.user_id, '/help')

        @self.client.on(events.NewMessage(from_users=self.user_id))
        async def handler(event):
            with open('session.txt', 'w', encoding='utf8') as f:
                f.write(event.message.text)
            await self.client.disconnect()

        await self.client.run_until_disconnected()

    def get(self):
        with self.client:
            self.client.loop.run_until_complete(self.main())


if __name__ == '__main__':
    tel_p = Tel_Proxy()
    tel_p.get()
