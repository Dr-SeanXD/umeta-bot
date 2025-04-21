import csv

import discord
from discord import app_commands
from discord.ext import commands
import pandas as pd
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os

TOKEN = os.getenv("DISCORD_TOKEN")

mod = ["ulun_umetafounder", "dr.seanxd", "cc8029", "feifei_gl", "benny9940", "ambish_creature"]

# /linkaccess
team_name = ["ulun_umetafounder", "dr.seanxd", "feifei_gl"]

# /inquire、/save
official_name = ["ulun_umetafounder", "dr.seanxd", "cc8029", "feifei_gl", "og_legacy", "benny9940", "ambish_creature"]

discord_link = {"ulun_umetafounder": 9487, "dr.seanxd": 9487, "feifei_gl": 9487}

# client 是跟 Discord 連接，intents 是要求機器人的權限
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

button = {'blue': discord.ButtonStyle.primary, 'red': discord.ButtonStyle.red, 'green': discord.ButtonStyle.green,
          'grey': discord.ButtonStyle.grey}


def isBoss(interaction: discord.Interaction):
    if interaction.user.name == "ulun_umetafounder":
        return True
    return False


def isOfficial(interaction: discord.Interaction):
    if interaction.user.name in official_name:
        return True
    return False


def isTeam(interaction: discord.Interaction):
    if interaction.user.name in team_name:
        return True
    return False


def isMod(interaction: discord.Interaction):
    if interaction.user.name in mod:
        return True
    return False


@bot.tree.command(name="giveofficialpoints", description="Give official points!")
@app_commands.check(isTeam)
async def giveofficialpoints(interaction: discord.Interaction, name: str, money: int):
    if name in official_name:
        newFile = []
        with open('Officials data.csv', newline='') as csvfile:
            files = csv.DictReader(csvfile)
            for file in files:
                if file['Name'] == name:
                    file['Official Points'] = str(int(file['Official Points']) + money)
                newFile.append(file)
            csvfile.close()
            df = pd.DataFrame(newFile)
            df.to_csv("Officials data.csv")
            my_channel = await interaction.guild.fetch_channel(1226480302457749548)
        await my_channel.send(f"{interaction.user.name} gave **{name}** **{str(money)}** official points!")
        await interaction.response.send_message(f"Successfully gave {name} {str(money)} official points!",
                                                ephemeral=True)
    else:
        await interaction.response.send_message("Error! Invalid name!", ephemeral=True)

password = "benny"

@bot.tree.command(name="inquire", description="Check the official points!")
@app_commands.check(isOfficial)
async def inquire(interaction: discord.Interaction):
    name = interaction.user.name
    if name in official_name:
        with open('Officials data.csv', newline='') as csvfile:
            files = csv.DictReader(csvfile)
            for file in files:
                if file['Name'] == name:
                    await interaction.response.send_message(
                        f"You currently have **{file['Official Points']}** official points!", ephemeral=True)
                    break
            csvfile.close()


@bot.tree.command(name="linkaccess", description="Give certain users access to send discord server invites temporaily!")
@app_commands.check(isTeam)
async def linkaccess(interaction: discord.Interaction, name: str, time: int):
    if name in mod:
        await interaction.response.send_message(f"{name} is an official member.")
    else:
        if name in discord_link:
            discord_link[name] = discord_link[name] + time
        else:
            discord_link[name] = time
        await interaction.response.send_message(f"{name} now has {str(time)} to send discord server invites!")


async def ucoinsearchch(interaction: discord.Interaction):
    name = interaction.user.name
    error = True
    with open('UCoin Query.csv', newline='') as csvfile:
        files = csv.DictReader(csvfile)
        for file in files:
            if file['Name'] == name:
                await interaction.response.send_message(f"您現在有 {file['UCoin']} UCoin!", ephemeral=True)
                error = False
                break
        if error:
            await interaction.response.send_message("您目前沒有 UCoin，關注並參與 UMETA 活動以獲得 UCoin!",
                                                    ephemeral=True)
        csvfile.close()


async def ucoinsearcheng(interaction: discord.Interaction):
    name = interaction.user.name
    error = True
    with open('UCoin Query.csv', newline='') as csvfile:
        files = csv.DictReader(csvfile)
        for file in files:
            if file['Name'] == name:
                await interaction.response.send_message(f"You currently have {file['UCoin']} UCoin!", ephemeral=True)
                error = False
                break
        if error:
            await interaction.response.send_message(
                "You currently don't have UCoin! Attend UMETA events to earn some UCoin!",
                ephemeral=True)
        csvfile.close()


@bot.tree.command(name="queryucoinchart", description="Create UCoin Query System!")
@app_commands.check(isTeam)
async def queryucoinchart(interaction: discord.Interaction):
    view = discord.ui.View()

    ch = discord.ui.Button(
        label="點我查詢 UCoin 數量！",
        style=button['blue'],
        row=0
    )
    ch.callback = ucoinsearchch
    view.add_item(ch)

    eng = discord.ui.Button(
        label='Click me to query UCoin amount!',
        style=button['green'],
        row=1
    )
    eng.callback = ucoinsearcheng
    view.add_item(eng)

    await interaction.response.send_message(
        "點擊以下按鈕來查詢 UCoin 數量！\nClick the buttons down below to query your UCoin amount!", view=view)


async def button_callbackP(interaction: discord.Interaction):
    newFile = []
    name = interaction.user.name
    with open('Pizza Day.csv', newline='') as csvfile:
        files = csv.DictReader(csvfile)
        user = {'UserID': interaction.user.id, "UserName": name, 'Pizza': 'Pepperoni'}
        add = True
        for file in files:
            if file['UserName'] == name:
                add = False
            newFile.append(file)
        if add:
            newFile.append(user)
            await interaction.response.send_message("你投給了臘腸披薩 Pepperoni!!!", ephemeral=True)
        else:
            await interaction.response.send_message("您之前已進行投票了，請等待投票時間截止後公布投票結果！",
                                                    ephemeral=True)
        csvfile.close()
        df = pd.DataFrame(newFile)
        df.to_csv("Pizza Day.csv")


async def button_callbackH(interaction: discord.Interaction):
    newFile = []
    name = interaction.user.name
    with open('Pizza Day.csv', newline='') as csvfile:
        files = csv.DictReader(csvfile)
        user = {'UserID': interaction.user.id, "UserName": name, 'Pizza': 'Hawaiian'}
        add = True
        for file in files:
            if file['UserName'] == name:
                add = False
                break
            newFile.append(file)
        if add:
            newFile.append(user)
            role = interaction.guild.get_role(1236345746056286300)
            await interaction.user.add_roles(role)
            await interaction.response.send_message("你投給了夏威夷披薩 Hawaiian!!!", ephemeral=True)
            df = pd.DataFrame(newFile)
            df.to_csv("Pizza Day.csv")
        else:
            await interaction.response.send_message("您之前已進行投票了，請等待投票時間截止後公布投票結果！",
                                                    ephemeral=True)
        csvfile.close()


async def button_callbackM(interaction: discord.Interaction):
    newFile = []
    name = interaction.user.name
    with open('Pizza Day.csv', newline='') as csvfile:
        files = csv.DictReader(csvfile)
        user = {'UserID': interaction.user.id, "UserName": name, 'Pizza': 'Margherita'}
        add = True
        for file in files:
            if file['UserName'] == name:
                add = False
            newFile.append(file)
        if add:
            newFile.append(user)
            await interaction.response.send_message("你投給了瑪格麗特披薩 Margherita!!!", ephemeral=True)
        else:
            await interaction.response.send_message("您之前已進行投票了，請等待投票時間截止後公布投票結果！",
                                                    ephemeral=True)
        csvfile.close()
        df = pd.DataFrame(newFile)
        df.to_csv("Pizza Day.csv")


@bot.tree.command(name="pizza", description="Pizza Vote Test!")
@app_commands.check(isTeam)
async def pizza(interaction: discord.Interaction):
    view = discord.ui.View()

    Pepperoni = discord.ui.Button(
        label="臘腸披薩 Pepperoni",
        style=discord.ButtonStyle.primary,
        row=0
    )
    Pepperoni.callback = button_callbackP
    view.add_item(Pepperoni)

    Hawaiian = discord.ui.Button(
        label="夏威夷披薩 Hawaiian",
        style=discord.ButtonStyle.red,
        row=1
    )
    Hawaiian.callback = button_callbackH
    view.add_item(Hawaiian)

    Margherita = discord.ui.Button(
        label="瑪格麗特披薩 Margherita",
        style=discord.ButtonStyle.grey,
        row=2
    )
    Margherita.callback = button_callbackM
    view.add_item(Margherita)

    await interaction.response.send_message("選 Pizza Time!", view=view)


@bot.event
async def on_message(message):
    msg = message.content
    if message.author == bot.user:
        if '點擊以下按鈕來查詢 UCoin 數量！' in msg:
            newFile = []
            with open('Loop Message.csv', newline='') as csvfile:
                files = csv.DictReader(csvfile)
                for file in files:
                    if file['Usage'] == 'UCoin':
                        file['ID'] = message.id
                    newFile.append(file)
                csvfile.close()
                df = pd.DataFrame(newFile)
                df.to_csv("Loop Message.csv")
        return
    if "discord.gg" in msg:
        name = str(message.author)
        if name not in discord_link.keys() or discord_link[name] <= 0:
            await message.delete()
            await message.channel.send(
                f"{message.author.mention}你的訊息中含有其他Discord伺服器的邀請連結，違反了本伺服器的規章第三條。\nYour message contains other discord server's invite link(s). This violates the third amendment of this server's rules.")
        else:
            if discord_link[name] != 9487:
                discord_link[name] = discord_link[name] - 1


# 調用 event 函式庫
@bot.event
async def on_ready():
    scheduler = AsyncIOScheduler()

    # scheduler.add_job(joinUs, CronTrigger(hour="12", minute="0", second="0"))

    scheduler.start()

    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")

hi = input()

if hi == password:
    bot.run(TOKEN)