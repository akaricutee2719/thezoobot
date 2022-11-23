import discord
import os
import time
import random
from money import money_banana
from discord.ext import commands
intents = discord.Intents.all()
intents.members = True
#-----------------
p1 = 3.6
p2 = 4.7
p3 = 5.6
p4 = 6.7
p5 = 7.4
p6 = 7.4
#-----------------
client = commands.Bot(command_prefix="tz!",intents=intents)
@client.event 
async def on_ready():
    print("Bot ready!")
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("Bot đang trong phiên bản BETA nên một số lệnh có thể chưa hoàn chỉnh, thông cảm :banana: !")
@client.command()
async def o(context):
    exit()
@client.command()
async def tkb(ctx):
    with open('assets\\image\\thoi_khoa_bieu.jpg', 'rb') as pic:
        picture = discord.File(pic)
    await ctx.send(file=picture)
@client.command()
async def Vu(ctx):
    await ctx.send("Vu da den.")
@client.command()
async def crm(ctx,team_a, team_b, *,tournament):
    with open("match_log\\created_time.tzf", 'r') as f:
        id_match = int(f.read())
    dirName = f'match_log/{id_match}'
    os.mkdir(dirName)
    times = id_match + 1
    answers = f"{team_a} v {team_b} tại {tournament}"
    s = open("match_log\\created_time.tzf", 'w')
    s.write(str(times))
    match_2=  open(f"match_log\\{id_match}\\{id_match}.txt", "w")
    match_2.write('')
    ra = (f"match_log\\{id_match}\\name_{id_match}.txt", "w")
    ra.write(f"{team_a} v {team_b} tại {tournament}")
    await ctx.send(f'Đã tạo log trận đấu {answers} với id {id_match} !')
@client.command()
async def members(ctx):
    for guild in client.guilds:
        for member in guild.members:
            name_1 = str(member)
            name = name_1[-4:]
            if not os.path.exists(f'assets\\information\\{name}.txt'):
                with open(f'assets\\information\\{name}.txt', 'w') as money_banana : 
                    money_banana.write(str(0))
@client.command()
async def members__to_buy_gun(ctx):
    for guild in client.guilds:
        for member in guild.members:
            name_1 = str(member)
            name = name_1[-4:]
            if not os.path.exists(f'gun\\ak47\\{name}.txt'):
                with open(f'gun\\ak47\\{name}.txt', 'w') as gun : 
                    gun.write(str(0))
            if not os.path.exists(f'gun\\desert_eagle\\{name}.txt'):
                with open(f'gun\\desert_eagle\\{name}.txt', 'w') as gun_2 : 
                    gun_2.write(str(0))
@client.command()
async def match_id(ctx, match_id):
    with open(f"match_log\\{match_id}.txt", 'r') as f:
        await ctx.send(f.read())
@client.command(aliases = ['wantbanana'])
async def give(ctx,tag_given,money):
    tag = str(ctx.author.discriminator)
    await ctx.send(money_banana.chuyen_tien(tag, tag_given, money))
@client.command()
async def cash(ctx):   
    tag = str(ctx.author.discriminator)
    await ctx.send(money_banana.kiem_tra(tag))
    # money_in_txt = open(f'D:\\coding stuff\\discord bot\\assets\\information\\{tag}.txt')
    # money= money_in_txt.read()
    # await ctx.send(f"Số banana của bạn hiện tại là **{money}** banana !")
@client.command()
async def lode(ctx,money, num):
    pts  = random.randint(0,100)
    print(pts)
    tag = str(ctx.author.discriminator)
    money_in_txt = open(f'assets\\information\\{tag}.txt')
    money_left_before= money_in_txt.read()
    if int(money) > int(money_left_before):
        await ctx.send("Bạn không đủ banana để chơi !")
    elif int(money) <= 0:
        await ctx.send("Giá trị không đúng !")
    elif not money.isdigit():
        await ctx.send("Giá trị không đúng !")
    elif int(money) > 1000000:
        await ctx.send("Mỗi lần chơi chỉ được tiêu ít hơn 1 triệu banana !")
    elif int(num) <0 or int(num) > 100 :
        await ctx.send("Nhập số từ 0-100 !")
    else: 
        await ctx.send("Thử vận may ... (thắng x20 đấy) !!!")
        time.sleep(3.5)
        if int(num) == int(pts):
            money_given = int(money) * 20
            money_given_in = int(money_left_before) + int(money_given)

            await ctx.send(f"Chúc mừng, bạn đã thắng **{int(money_given):,d}** :banana:, số đó là **{pts}** !")
            with open(f'assets\\information\\{tag}.txt', 'w') as money_banana : 
                money_banana.write(str(money_given_in))
        else:
            money_given = int(money_left_before) - int(money)
            await ctx.send(f"Bạn đã thua **{int(money):,d}** :banana:, số đó phải là **{pts}** !")
            with open(f'assets\\information\\{tag}.txt', 'w') as money_banana : 
                money_banana.write(str(money_given))
@client.command()
async def banana(ctx,*,money):
    tag = str(ctx.author.discriminator)
    money_in_txt = open(f'assets\\information\\{tag}.txt')
    money_left_before= money_in_txt.read()
    
    if int(money) > int(money_left_before):
        await ctx.send("Bạn không đủ banana để chơi !")
    elif int(money) <= 0:
        await ctx.send("Giá trị không đúng !")
    elif not money.isdigit():
        await ctx.send("Giá trị không đúng !")
    elif int(money) > 1000000:
        await ctx.send("Mỗi lần chơi chỉ được tiêu ít hơn 1 triệu banana !")
    else:
        money_left_after = int(money_left_before) - int(money)
        await ctx.send(f"Bạn đã cược **{int(money):,d}** :banana: ... ")
        pts = random.randint(0,1)
        pts = random.randint(0,1)
        time.sleep(4)
        if pts == 0:
            await ctx.send(f"Bạn đã thua **{int(money):,d}** :banana: !")
            with open(f'assets\\information\\{tag}.txt', 'w') as money_banana : 
                money_banana.write(str(money_left_after))
        elif pts ==1:
            money_give = int(money) * 2
            await ctx.send(f"Bạn đã thắng **{int(money_give):,d}** :banana: !")
            money_left_after = money_left_after + money_give
            with open(f'assets\\information\\{tag}.txt', 'w') as money_banana : 
                money_banana.write(str(money_left_after))
@client.command()
async def VAR(ctx,*,question):
    await ctx.send(f'CHECKING VAR - POSSIBLE **{question}** ...')
    time.sleep(3)
    pts = random.randint(0,1)
    pts = random.randint(0,1)
    if pts == 0:
        await ctx.send(f'CHECKING VAR - POSSIBLE **{question}** IS FALSE')
    else:
        await ctx.send(f'CHECKING VAR - POSSIBLE **{question}** IS TRUE')
@client.command()
async def PhucSadBoiDiBanMaTuy(ctx):
    with open('assets\\image\\easter_egg_2.png', 'rb') as pic:
        picture = discord.File(pic)
    await ctx.send('coward.',file=picture)
@client.command()
async def calc(ctx, money):
    global p1, p2, p3, p4, p5, p6 
    await ctx.send(f""" **RESULT : **
    :arrow_forward: 1 Goal : **{round(int(money)*p1):,d}** :banana: | **x{p1}**
    :arrow_forward: 2 Goals : **{round(int(money)*p2):,d}** :banana: | **x{p2}**
    :arrow_forward: 3 Goals : **{round(int(money)*p3):,d}** :banana: | **x{p3}**
    :arrow_forward: 4 Goals : **{round(int(money)*p4):,d}** :banana: | **x{p4}**
    :arrow_forward: 5 Goals : **{round(int(money)*p5):,d}** :banana: | **x{p5}**
    :arrow_forward: 6 Goals or more : **{round(int(money)*p6):,d}** :banana: | **x{p6}**
    ***Chốt sau 23:00 22-11**
    """)
@client.command(aliases=['shop','cuahang'])
async def hien_cua_hang(ctx, arg):
    if arg == 'menu':
        await ctx.send(
            ''':shopping_cart: **SHOP the zoo DISCORD SERVER**\n
            :arrow_right: If you want to purchase **gun or bullet**, using the argument **"gun"** after **tz!shop/cuahang**
            :arrow_right: If you want **gun license test**, using the argument **"gun_license"** after **tz!shop/cuahang**
            :arrow_right: ATTENTION: **EVERYTHING HERE IS IN BETA VERSION !** 
            ''')
    elif arg == 'gun':
        await ctx.send("coward.")
    elif arg == 'gun_license':
        await ctx.send("solve this : -5 x y = ym")
    else: 
        await ctx.send("Wrong argument, try again !")
client.run('MTA0MDk2NjQ1MjE4MzgzODg0Mg.GFpQvk.0a5zd_JF_vSwp3g86pLX0wtcb9QxYX761Ld0Jg')
