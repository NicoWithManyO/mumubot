import discord
from discord.ext import commands
from discord.commands import slash_command
from Helpers.discordUtils import guildsInit

class GuildCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
     
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self} ready")
        await guildsInit(self.bot)

def setup(bot):
    bot.add_cog(GuildCommand(bot))