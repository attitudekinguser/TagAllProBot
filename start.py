@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("** I am member Tagger **, I can Tag almost all members in group or channel 🤓\nClick **/help** for more infomation.\n\n Here is my [Developer👨‍💻](https://t.me/ABOUTVEDMAT)",
                    buttons=(
                      [Button.url('📣 UPDATE CHANNEL', 'https://t.me/LOVELY_ROBOTS')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Hey 🤓 I Am Member Tagger \n\n You can Tag members by using Commands shown below,\n\n /all text \n\n @all text \n\n #all text**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('📣 UPDATE CHANNEL', 'https://t.me/LOVELY_ROBOTS')]
                    ),
                    link_preview=False
                   )
  
