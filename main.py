import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def rand(ctx):
    integer_list = [100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 208, 
                    226, 300, 301, 302, 303, 304, 305, 307, 308, 400, 401, 402, 403, 404
                    , 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 
                    418, 420, 421, 422, 423, 424, 425, 426, 428, 429, 431, 444, 450, 451
                    , 497, 498, 499, 500, 501, 502, 503, 504, 506, 507, 508, 509, 510, 
                    511, 521, 522, 523, 525, 530, 599]
    def pick_random_integer(integer_list):
      return random.choice(integer_list)
    random_integer = pick_random_integer(integer_list)
    await ctx.send(f"https://http.cat/{random_integer}.jpg")
@bot.event
async def on_message(message):
    bot_user = bot.user
    if bot_user in message.mentions:
        ctx = await bot.get_context(message)
        command = bot.get_command("rand")
        if command:
          await ctx.invoke(command)
    await bot.process_commands(message)

bot.run("MTE4NDE3NjI2NDAwNTgyMDQ2Ng.GP9n9b.dyOmLUKBAgMgFBR6rO7yiZz4MLZjczISdNIGbc")