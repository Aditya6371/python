import discord
import responses

async def send_message(message,user_message,is_private):
    try:
        response  = responses.handle_responses(user_message)
        await message.author.send(response) if is_private else await message.author.send(response)
    ## expect: print('Invalid Input')
    except: print('Invaild input..')

def run_discord_bot():
    TOKEN = 'MTA2Mzk4NTUzMjg3NjY0MDI4Nw.GZd6Nw.ZiR0NgPGzyxHgJ8dsJx4_rDucL1EJoeOJgUbAQ'
    client = discord.Client(intents=discord.Intents.default())


    @client.event
    async def on_ready():
        print(f'{client.user} is now running...')

    @client.event
    async def on_message(message):
        if message.author==client.user:
            return
            

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said '{user_message}'({channel})")

        if len(user_message)>0:
            if user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message,user_message,is_private=True)
            else:
                await send_message(message,user_message,is_private=False)

            
    client.run(TOKEN)    