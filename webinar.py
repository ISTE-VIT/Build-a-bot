import discord
import os
from keep_alive import keep_alive
server=discord.Client()


keywords=["purple","cheese","paper"]
@server.event
async def on_ready():
  print("The bot is running")
  general=server.get_channel(814035141047484419)
  await general.send("I am back online")


@server.event
async def on_message(message):
  if message.author==server.user:
    return

  channel=message.channel

  if message.content.startswith("!hello"):
    await channel.send("Hey! {0.mention}".format(message.author))

  if message.content.startswith("!math"):
    numbers=message.content.split(" ")
    print(eval(numbers[1]))
    await channel.send(numbers[1]+"="+str(eval(numbers[1])))

  if message.content.startswith("!announce"):
    announcement_channel=server.get_channel(842018629741707284)
    announcement=message.content.split(" ",1)[1]
    await announcement_channel.send(announcement)
    await message.add_reaction("👍")
  for i in keywords:
    if i in message.content:
      await message.delete()


@server.event
async def on_reaction_add(reaction,user):
  print(type(reaction))
    # channel=server.get_channel(842018629741707284)
    # await channel.send("laptop added")
  if(reaction.message.channel.id==842414168165318687) :
    if(str(reaction)=='💻'):
      techie_role=discord.utils.get(reaction.message.guild.roles,name="admin")
      await user.add_roles(techie_role)

keep_alive()
server.run(os.getenv('TOKEN'))
