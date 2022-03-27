import discord
import requests
import json

TOKEN = "TOKEN"


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'Подключен, готов показать вам пушистый комок счастья, по вашему усмотрению')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "кот" in message.content.lower():
            response = requests.get("https://api.thecatapi.com/v1/images/search")
            json_data = json.loads(response.text)
            url = json_data[0]["url"]
            print(url)
            await message.channel.send("чоткий котя")
            await message.channel.send(url)
        elif "кош" in message.content.lower():
            response = requests.get("https://api.thecatapi.com/v1/images/search")
            json_data = json.loads(response.text)
            url = json_data[0]["url"]
            print(url)
            await message.channel.send("чоткая котя")
            await message.channel.send(url)

        elif "пес" in message.content.lower():
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            json_data = json.loads(response.text)
            url = json_data["message"]
            print(url)
            await message.channel.send("чоткий песя")
            await message.channel.send(url)
        elif "пёс" in message.content.lower():
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            json_data = json.loads(response.text)
            url = json_data["message"]
            print(url)
            await message.channel.send("чоткий пёся")
            await message.channel.send(url)
        elif "псин" in message.content.lower():
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            json_data = json.loads(response.text)
            url = json_data["message"]
            print(url)
            await message.channel.send("чоткая псина")
            await message.channel.send(url)
        elif "соба" in message.content.lower():
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            json_data = json.loads(response.text)
            url = json_data["message"]
            print(url)
            await message.channel.send("чоткая собака")
            await message.channel.send(url)
        else:
            await message.channel.send("Спасибо за сообщение, но мой создатель видимо написал не все возможные вариации склонений и спряжений для слов кот, пес, собака и кошка. Так что я вас не понял"
                                       "\n\n либо вы написали что то другое")


client = YLBotClient()
client.run(TOKEN)
