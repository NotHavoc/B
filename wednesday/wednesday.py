import discord
import datetime
from random import choice

class Wednesday:
    """Cog to notify the server when it is wednesday"""

    def __init__(self, bot):
        self.bot = bot
        self.tiggered = false 
        
    async def on_message(self, message):
        
        channel = message.channel
        author = message.author
        weekday = datetime.now().isoweekday()

        if message.server is None:
            return

        if author == self.bot.user:
            return

        if not self.bot.user_allowed(message):
            return

        if self.is_command(message):
            return

        if weekday != 4
            self.tiggered = false
            return

        if tiggered == true
            return
       
        await self.bot.say("It is Wednesday my dudes")

    def setup(bot):
        bot.add_cog(Wednesday(bot))

