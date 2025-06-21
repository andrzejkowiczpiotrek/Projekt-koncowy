import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

ekoporady = [
    "Zakręcaj wodę podczas mycia zębów – to oszczędza nawet 6 litrów na minutę!",
    "Wybieraj produkty lokalne i sezonowe – zmniejszasz ślad węglowy transportu.",
    "Zamiast auta – wybierz rower lub komunikację miejską.",
    "Unikaj jednorazowego plastiku – używaj wielorazowych toreb i butelek."
]

ekofakty = [
    "Plastik potrzebuje nawet 1000 lat, by się rozłożyć.",
    "1 drzewo może w ciągu roku pochłonąć około 20 kg CO2.",
    "Oceany pochłaniają około 30% emitowanego CO2.",
    "Recykling jednej puszki aluminiowej oszczędza energię potrzebną do działania telewizora przez 3 godziny."
]

zerowaste_przypomnienia = [
    "🛍️ Pamiętaj, by zabrać swoją torbę na zakupy!",
    "🥤 Unikaj plastikowych słomek – używaj stalowych lub bambusowych.",
    "🍽️ Zamawiasz jedzenie? Dodaj notatkę: *„bez sztućców i serwetek”*.",
    "📦 Daj drugie życie pudełkom – użyj ich do przechowywania."
]

ekoquizy = [
    {
        "pytanie": "Ile lat rozkłada się plastikowa butelka?",
        "odpowiedzi": {"a": "100", "b": "450", "c": "50"},
        "poprawna": "b"
    },
    {
        "pytanie": "Co ma mniejszy ślad węglowy?",
        "odpowiedzi": {"a": "Warzywa sezonowe", "b": "Mięso wołowe", "c": "Ryż z importu"},
        "poprawna": "a"
    },
    {
        "pytanie": "Ile drzew pochłania tonę CO₂ rocznie?",
        "odpowiedzi": {"a": "10", "b": "50", "c": "100"},
        "poprawna": "c"
    }
]

@bot.event
async def on_ready():
    print(f"🌿 Ekobot aktywny jako {bot.user}")

@bot.command()
async def ekoporada(ctx):
    await ctx.send(f"♻️ Ekoporada: {random.choice(ekoporady)}")

@bot.command()
async def ekofakt(ctx):
    await ctx.send(f"🌍 Ekofakt: {random.choice(ekofakty)}")

@bot.command()
async def zerowaste(ctx):
    await ctx.send(f"🧼 Przypomnienie Zero Waste: {random.choice(zerowaste_przypomnienia)}")

@bot.command()
async def ekoquiz(ctx):
    quiz = random.choice(ekoquizy)
    pytanie = quiz["pytanie"]
    odp = quiz["odpowiedzi"]
    msg = (
        f"🧠 **Ekoquiz!**\n{pytanie}\n"
        f"a) {odp['a']}\n"
        f"b) {odp['b']}\n"
        f"c) {odp['c']}\n"
        "Odpowiedz wpisując `!odpowiedz a/b/c`"
    )
    # Zapamiętaj quiz użytkownika
    bot.last_quiz = quiz
    await ctx.send(msg)

@bot.command()
async def odpowiedz(ctx, wybor: str):
    if not hasattr(bot, 'last_quiz'):
        await ctx.send("❌ Najpierw wpisz `!ekoquiz`.")
        return
    if wybor.lower() == bot.last_quiz["poprawna"]:
        await ctx.send("✅ Dobrze! Brawo! 💚")
    else:
        await ctx.send(f"❌ To niepoprawna odpowiedź. Prawidłowa to: `{bot.last_quiz['poprawna']}`.")

@bot.command()
async def co2(ctx, km: float):
    co2_na_km = 0.12  # kg CO₂ na 1 km samochodem
    oszczednosc = km * co2_na_km
    await ctx.send(f"🚶‍♂️ Jeśli przejdziesz {km:.1f} km pieszo zamiast jechać autem, zaoszczędzisz {oszczednosc:.2f} kg CO₂!")

# ⛔ Wklej swój token tutaj:
bot.run("")
