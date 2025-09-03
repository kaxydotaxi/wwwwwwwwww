import discord
import re
import requests

TOKEN = "MTE2MDQzMDE3ODg4ODA1Njg1NA.Gb7-DC.egArlcQLACHEScr6KqNp2MfrnFv5TUxwgHMLd0"  # ⚠️ token da sua conta pessoal
CHANNELS = [
    1375597674539122718,
    1361250135719280842,
    1375597664829181994
]  # IDs dos canais que você passou

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

def mudar_username(novo_nome):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }
    data = {
        "username": novo_nome
    }
    r = requests.patch(url, headers=headers, json=data)
    if r.status_code == 200:
        print(f"✅ Username alterado para {novo_nome}")
    else:
        print(f"❌ Erro ao mudar username: {r.status_code} {r.text}")

@client.event
async def on_message(message):
    if message.channel.id in CHANNELS and message.author.bot:
        # procura algo tipo: "✔️ zxb | Is available..."
        match = re.search(r"✔️ (\w+)", message.content)
        if match:
            nick = match.group(1)
            print(f"Nick detectado: {nick}")
            mudar_username(nick)

client.run(TOKEN, bot=False)  # ⚠️ Self-bot
