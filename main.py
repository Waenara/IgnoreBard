import os
try:
    import bardapi
    import discord
    from discord.ext import commands
    import requests
    from bardapi import Bard
    import json
except:
    os.system('pip install -U discord.py-self==1.9.2 requests json')
    os.system('pip install -U bardapi')
    import discord
    from discord.ext import commands
    import bardapi
    import requests
    from bardapi import Bard
    import json

f = open("config.json", "r", encoding="utf-8").read()
json1 = json.loads(f)

if json1["token-bard"] == "Куки барда сюда" or json1["token-discord"] == "Токен дискорд аккаунта сюда":
    print("Заполни config.json сперва")
    exit()

bot = commands.Bot(command_prefix="",
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)



def bard(message):
    token = json1["token-bard"]
    bard = Bard(token=token)
    val = bard.get_answer(message)['content']
    return val
@bot.event
async def on_connect():
    print('Logged on as', bot.user)
@bot.event
async def on_message(message):
    if message.guild != None:
        return
    if message.author == bot.user:
        return

    users1 = open("users.txt", "r")
    users = users1.readlines()
    match = False


    for i in users:
        if i.startswith("--") or i == "1125078080046768138":
            return

        user = bot.get_user(id=int(i))
        if message.author == user:
            match = True


    if match == False:
        return

    users1.close()
    prompt = bard(message.content)
    await message.reply(prompt)






try: bot.run(json1["token-discord"])
except: print("Что-то пошло не так. Скорее всего вы ввели неправильный токен.")