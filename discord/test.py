import discord

TOKEN = "OTU3NjUzODUzNDI2MzE1MzQ0.YkB6pw.P2RgoifCvF592nxwSWbhIDuBayU"


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if message.author == self.user:
            return
        await message.channel.send("Спасибо за сообщение")


client = YLBotClient()
client.run(TOKEN)