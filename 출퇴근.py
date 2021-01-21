import discord

client = discord.Client()
token = 'Nzk3NjU1MTA4Mzg0NzE4ODg4.X_poNQ.tUk46ohNxWMbu60zTRRs_7B4F88'

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('출퇴근 관리중')
    await client.change_presence(status=discord.Status.online, activity=game)

    
@client.event
async def on_message(message):
    if message.content.startswith("!출근"):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0x80E12A)
                channel = 797656744385314826
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='ARIA 출퇴근 알림', value= f'<@{message.author.id}> 가 출근 하였습니다.')
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/759623750391038012/801792864551174194/1.gif")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

    if message.content.startswith("!퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0xFF0000)
                channel = 797656744385314826
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='ARIA 출퇴근 알림', value= f'<@{message.author.id}> 가 퇴근 하였습니다.')
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/759623750391038012/801792864551174194/1.gif")
                await client.get_channel(int(channel)).send(embed=embed)
        except:
            pass

client.run(token)