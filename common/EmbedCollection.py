from typing import List
import discord

class EmbedCollection: # 임베드 모음

    class 내전모집임베드(discord.Embed): # 내전모집 임베드
        def __init__(self, participants : List[discord.User], owner : discord.User, 시작시간: str):
            super().__init__(
                title="인간 시대의 끝이 도래했다-",
                description="RUNTERRA 내전을 시작합니다-",
                color=discord.Color.blue()
            )
            self.add_field(
                name="모집 소환사",
                value=f"{owner.mention} \n 소환사가 내전을 모집합니다-",
                inline=True
            )
            self.add_field(
                name="내전 시작 시간",
                value=시작시간,
                inline=True
            )   
            self.add_field(
                name = "참가 소환사",
                value = "\n".join([
                    u.mention for u in participants
                ])
            )
    
    class 내전진행대기중Embed(discord.Embed): # 내전 진행 대기중 임베드
        def __init__(self, bot):
            super().__init__(
                title="내전 진행 대기중-",
                description="",
                color=discord.Color.greyple()
            )

            channel_id = 1205095960464859200 # 대기음성채널 ID
            channel = bot.get_channel(channel_id)
            members = channel.members
            member_names = [member.name for member in members]

            self.add_field(
                name = "진행 대기 소환사",
                value = "\n".join(member_names),
                inline = False
            )

    class 내전진행Embed(discord.Embed): # 내전진행 임베드
        def __init__(self):
            super().__init__(
                title="test",
                description="test",
                color=discord.Color.greyple()
            )