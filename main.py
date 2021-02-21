from discord import File
from discord.ext import commands
from helpers.utils import *
bot = commands.Bot(command_prefix='!')

path_not_message_mute = "saved_objects/not_message_mute.wtf"
not_to_message_on_mute = []


@bot.event
async def on_ready():
    for item in get_list_from_path(path_not_message_mute):
        not_to_message_on_mute.append(item)
    print("I'm in!")


@bot.command()
async def mute(ctx):
    member = ctx.message.author
    if member in not_to_message_on_mute:
        print(member)
        not_to_message_on_mute.remove(member)
        await ctx.message.channel.send("Du wirst wieder über dein muten benachrichtigt.")
    else:
        not_to_message_on_mute.append(member)
        await ctx.message.channel.send("Du wirst nicht mehr über dein muten benachrichtigt.")
    save_list_to_path(not_to_message_on_mute, path_not_message_mute)


@bot.command()
async def ordnungsruf(ctx):
    mentioned_users = ctx.message.mentions
    if len(mentioned_users) == 0:
        await ctx.message.channel.send("Du solltest auch jemanden erwähnen ...")
    elif len(mentioned_users) > 1:
        with open("pictures/ich_rufe_zur_ordnung.png", "rb") as picture:
            picture = File(picture)
            await ctx.message.channel.send("Bitte nur eine Person auf einmal!", file=picture)
    else:
        with open("pictures/ich_rufe_zur_ordnung.png", "rb") as picture:
            picture = File(picture)
            for user in mentioned_users:
                await user.send(file=picture)


@bot.event
async def on_voice_state_update(member, before, after):
    print(not_to_message_on_mute)
    if not before.self_mute and after.self_mute and member.id not in not_to_message_on_mute:
        print(member.id)
        print(not_to_message_on_mute)
        await member.send("Du bist gemuted! >:(")


with open("key.txt", "r") as file:
    key = file.read()
bot.run(key)
