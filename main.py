from http import client
import discord
from discord.ext import commands
from discord.ui import View, Button
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()  # All but the THREE privileged ones
intents.message_content = True  # Subscribe to the Message Content intent
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)  # Pass the intents into your commands.Bot or discord.Client

# @bot.event
# async def on_message(message):
#     if message.channel.id == 918110120494387200:
#         print('Message :'+message.content)
#     await bot.process_commands(message)

#@bot.command()
# async def test(ctx):
#     button = Button(label="Subscribe", style = discord.ButtonStyle.url, url = "https://www.youtube.com/poisonymous", emoji="<:YouTube:960833722725335061>")
#     view = View()
#     view.add_item(button)
#     await ctx.send("**📺 YOUTUBE**", view=view)

@bot.command()
async def rolecheck(ctx, role: discord.Role):
    names = [member.display_name for member in role.members]
    t=''
    for i in names:
        t+=i+'\n'
    await ctx.send('```\n'+t+'\n```')

# @bot.command(pass_context=True)  
# async def getuser(ctx, role: discord.Role):
#     role = role
#     guild = bot.get_guild(912740687382982756)
#     if role is None:
#         await ctx.send('There is no "mod" role on this server!')
#         return
#     empty = True
#     for member in guild.members:
#         if role in member.roles:
#             await ctx.send("{0.name}: {0.id}".format(member))
#             empty = False
#     if empty:
#         await ctx.send("Nobody has the role {}".format(role.mention))


bot.run('OTYwNTQ5NTUyNzkwODU5ODE2.YksDew.gckPpY1Ye4V2bjjE-NuVqS3zZ6A')
