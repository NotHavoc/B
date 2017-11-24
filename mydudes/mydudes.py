import discord
from discord.ext import commands

class Mydudes:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("It is Wednesday my dudes.")

def setup(bot):
    bot.add_cog(MYdudes(bot))
