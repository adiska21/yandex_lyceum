import discord
import asyncio

TOKEN = "TOKEN"


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'Подключен, готов поcтавить вам таймер')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if "set_timer" in message.content.lower():
            text = message.content.split(" ")
            print(text)
            text.pop(0) and text.pop(0) and text.pop(1) and text.pop(1) and text.pop(2)
            print(text)
            timeout = float(text[0]) * 3600 + float(text[1]) * 60
            await asyncio.sleep(timeout)
            await message.channel.send("⏰момент X⏰")
        else:
            await message.channel.send("не правильный формат ввода\n\n"
                                       "правильно:\n```set_timer{команда} in {кол-во часов} hour"
                                       " and {кол-во минут} minutes```")


client = YLBotClient()
client.run(TOKEN)