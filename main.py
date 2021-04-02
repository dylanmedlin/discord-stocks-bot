from discord.ext import commands
import yahoo_fin.stock_info as si
import config

bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def stock(ctx, stock):
    data = si.get_quote_table(stock)
    price = data['Quote Price']
    open = data['Previous Close']
    change = ((price - open) / open) * 100
    msg = await ctx.channel.send('Current: ${:0.2f}\nChange: {:0.2f}%'.format(price, change))
    print(stock)
    print('Current: ${:0.2f}\nChange: {:0.2f}%'.format(price, change))
    print('------')
    if price > open:
        await msg.add_reaction('🚀')
    else:
        await msg.add_reaction('🔻')


bot.run(config.token)
