import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"🥓 Bacon Bot is online as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("🥓 Pong! Bacon Bot is alive!")


@bot.command()
async def info(ctx):
    await ctx.send(
        "🥓 **Bacon Clan**\n"
        "🔪 Knife Only\n"
        "👥 2 Members\n"
        "✨ Maximum Aura"
    )


@bot.command()
async def rules(ctx):
    await ctx.send(
        "**🥓 BACON CLAN RULES 🥓**\n\n"
        "1. No scamming\n"
        "2. No NSFW\n"
        "3. Light swearing only\n"
        "4. No bullying or harassment\n"
        "5. Stay on-topic\n"
        "6. No self-advertising\n"
        "7. No impersonation\n"
        "8. Be kind and respectful\n"
        "9. 🔪 KNIFE ONLY\n"
        "10. Use `BACON_(YOUR_DISPLAY_NAME)`"
    )


@bot.command()
async def aura(ctx):
    await ctx.send("✨ Your aura level is: **MAXIMUM**")


@bot.command()
async def bacon(ctx):
    await ctx.send("🥓🥓🥓 **BACON ATTACK!** 🥓🥓🥓")


@bot.command()
async def knife(ctx):
    await ctx.send("🔪 **KNIFE ONLY. NO GUNS.**")


if not TOKEN:
    raise ValueError("DISCORD_TOKEN is missing!")

bot.run(TOKEN)
