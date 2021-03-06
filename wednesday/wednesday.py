import os
import discord
import request
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from cogs.utils.chat_formatting import box, pagify, escape_mass_mentions
from random import choice

#import time
#import datetime

class Wednesday:
    """Cog to notify the server when it is wednesday"""

    def init(self, bot):
        self.bot = bot
        #self.triggered = false 

    def on_message(message):
        #reads server messages, if it is the first message of wednesday posts the notification
        channel = message.channel
        author = message.author
        weekday = 3
        #datetime.now().isoweekday()

        if(weekday == 3)
            await self.bot.say("It is Wednesday my dudes")

        else
            return

    def setup(bot):
        bot.add_cog(Wednesday(bot))

"""
import os
import discord
import request
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from cogs.utils.chat_formatting import box, pagify, escape_mass_mentions
#from random import choice

#import time
#import datetime

class Wednesday:
    #Cog to notify the server when it is wednesday

    def __init__(self, bot):
        self.bot = bot
        #self.triggered = false 
        
    async def on_message(self, message):
        #reads server messages, if it is the first message of wednesday posts the notification
        channel = message.channel
        author = message.author
       # weekday = datetime.now().isoweekday()
        weekday = 3

        if message.server is None:
            return

        if author == self.bot.user:
            return
        
        if not self.bot.user_allowed(message):
            return

        if self.is_command(message):
            return
        
        if (weekday != 3):
        #    self.tiggered = false
            return

        #if (triggered == true):
         #   return
      
        await self.bot.say("It is Wednesday my dudes")
        triggered = true

    def setup(bot):
        bot.add_cog(Wednesday(bot))

"""
