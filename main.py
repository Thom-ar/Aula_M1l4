import random
import discord
from discord.ext import commands

# Permissões do bot (precisa para ler mensagens)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


# 1) Comando mais simples: responde uma mensagem fixa
@bot.command()
async def ola(ctx):
    await ctx.send(f"Olá, {ctx.author.name}! 👋")


# 2) Comando com argumentos: soma dois números
@bot.command()
async def somar(ctx, a: int, b: int):
    await ctx.send(f"{a} + {b} = {a + b}")


# 3) Comando com random: dado de 6 lados
@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)
    await ctx.send(f"🎲 Você tirou: {numero}")


# 4) Comando com lista: sorteia uma resposta
@bot.command()
async def bola8(ctx, *, pergunta):
    respostas = ["Sim!", "Não.", "Talvez...", "Com certeza!", "Pergunte de novo depois."]
    await ctx.send(f"🎱 {random.choice(respostas)}")


# 5) Comando com condição: par ou ímpar
@bot.command()
async def parimpar(ctx, numero: int):
    if numero % 2 == 0:
        await ctx.send(f"{numero} é par!")
    else:
        await ctx.send(f"{numero} é ímpar!")


# 6) Comando com repetição: contagem regressiva
@bot.command()
async def contagem(ctx, inicio: int = 5):
    texto = ""
    for i in range(inicio, 0, -1):
        texto += f"{i}... "
    await ctx.send(texto + "🚀 Já!")


# 7) Comando com embed: cartão bonito com informações
@bot.command()
async def perfil(ctx):
    embed = discord.Embed(title="Meu perfil", color=discord.Color.blue())
    embed.add_field(name="Nome", value=ctx.author.name)
    embed.add_field(name="Servidor", value=ctx.guild.name)
    await ctx.send(embed=embed)


# Tratamento simples de erro (mostra try/except em ação)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Faltou um argumento! Exemplo: `!somar 2 3`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Valor inválido! Use números onde for pedido.")


bot.run("COLE_SEU_TOKEN_AQUI")
