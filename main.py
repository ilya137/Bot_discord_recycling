import discord
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

random_fact_plastic = ['Начиная с 1950-х годов человечество произвело 8,3 миллиардов тонн пластика. Только 9% из этой массы отправились на переработку.','Практически каждый кусочек произведённого пластика до сих пор где-то существует.','Каждый год 1 миллион морских птиц и 100 тысяч морских млекопитающих погибают из-за пластика.']

random_fact_paper = ['Бумагу можно есть!', 'Бумагу можно повторно перерабатывать до 5 раз без потери качества','Только в XVIII веке научились отбеливать бумагу']

random_fact_grass = ['Стекло это один из немногих материалов, которые могут быть переработаны на 100% при этом не теряя качества.','Стекло разлагается 1 миллион лет.','Когда разбивается стекло, трещина движется со скоростью 4828 км/ч.']

@bot.command()
async def grass(ctx):
    with open('images/grass.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    random_fact = random.choice(random_fact_grass)
    await ctx.send(random_fact)

@bot.command()
async def paper(ctx):
    with open('images/paper.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    random_fact = random.choice(random_fact_paper)
    await ctx.send(random_fact)

@bot.command()
async def plastic(ctx):
    with open('images/plastic.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    random_fact = random.choice(random_fact_plastic)
    await ctx.send(random_fact)

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def random_mem(ctx):
    memi = ['images/mem1.jpg', 'images/mem2.jpg', 'images/mem3.jpg']
    n = random.randint(1, 10)
    if n == 1:
        mem = 'images/mem1.jpg'
    elif n == 10 or n == 5:    
        mem = 'images/mem2.jpg'
    else: 
        mem = 'images/mem3.jpg'  
   # mem = random.choice(memi)
    with open(mem, 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)    

bot.run("MTE4ODQ0ODIyOTU2NjcyMjEzMA.GQaiqh.-IehZCCt3Ze14JpexeLgtHkP_ij21sjm5DLdGk")    
