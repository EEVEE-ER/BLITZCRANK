import discord
from discord.ext import commands
from discord import app_commands
from typing import List
from common.EmbedCollection import EmbedCollection

내전최대인원 : int = 1 #내전인원은 10명이 되어야 하는데, 우선 테스트로 2로 해놓음

class 내전모집(commands.Cog): #내전모집 클래스 정의
    def __init__(self, bot):
        self.bot = bot
        self.arstarstarst.current_participants = []
        self.embed_collection = EmbedCollection()
        
        
    @app_commands.command(name="내전모집", description="내전을 모집합니다-")  # '/내전모집' 커멘드
    @app_commands.describe(시작시간="'즉시 또는 PM 12시'와 같이 입력하세요-")
    async def 내전모집(self, interaction: discord.Interaction, 시작시간: str):
        user = interaction.user
        
        # 임베드 관련 부분
        embed = self.embed_collection.내전모집Embed(
            participants=[],
            owner = user,
            시작시간 = 시작시간
        )
        view = 내전모집View(
            bot=self.bot,
            owner = user,
            시작시간 = 시작시간,
            participants=[]
        ) # 내전모집view 클래스 버튼 호출

        self.bot.current_recruitment_message = await interaction.response.send_message(
            "@everyone",
            embed=embed,
            view=view
        ) 
        
        # 참가자 리스트 초기화
        self.bot.current_participants = []
            
class 내전처리():
    def 참가자추가():
        return

    def 참가자제거():
        return

class 내전모집View(discord.ui.View): # 내전모집view 클래스
    def __init__(self, bot, owner : discord.User,  시작시간 : str, participants : List[discord.User]):
        super().__init__(
            timeout=None
        )
        self.bot = bot
        self.participants = participants
        self.owner = owner
        self.시작시간 = 시작시간
        self.embed_collection = EmbedCollection()
        self.내전처리 = 내전처리()

    # '내전참가' 버튼
    @discord.ui.button(label='👋🏻 내전참가', style=discord.ButtonStyle.blurple, custom_id='join')
    async def join(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.내전처리
        participant = interaction.user

        # 이미 참가한 상태라면
        if participant in self.participants:
            await interaction.response.send_message(
                f"{participant.mention} 소환사님은 이미 내전 참가 중입니다-",
                ephemeral=True
            )
            return

        # 인원이 이미 가득 차 있으면
        if len(self.participants) >= 내전최대인원:
            await interaction.response.send_message(
                f"이미 {내전최대인원}명의 소환사가 모두 모집되어 있습니다-",
                ephemeral=True
            )
            return

        self.participants.append(participant)

        if len(self.participants) == 내전최대인원:
            # 새롭게 참가함으로써 인원이 가득차게되었다면
            await interaction.response.edit_message(
                embed = self.embed_collection.내전모집Embed(
                    owner = self.owner,
                    participants=self.participants,
                    시작시간 = self.시작시간,
                ),
                view = None # 버튼 비활성화
            )
            participants_mentions = ', '.join([user.mention for user in self.participants])
            new_message = f"`✔️ 내전모집이 완료되었습니다-`\n{participants_mentions} `소환사는` \n<#1205095960464859200> `채널로 입장해주세요-`"

            await interaction.channel.send(new_message, embed=self.embed_collection.내전진행대기중Embed(self.bot))
            
       
        else:
            # 정상적으로 참가
            await interaction.response.edit_message(
                embed = self.embed_collection.내전모집Embed(
                    owner = self.owner,
                    participants=self.participants,
                    시작시간 = self.시작시간,
                ),
            )

    # '참가취소' 버튼       
    @discord.ui.button(label='✊🏻 참가취소', style=discord.ButtonStyle.gray, custom_id='cancel_join')
    async def cancel_join(self, interaction: discord.Interaction, button: discord.ui.Button):
        participant = interaction.user

        # 참가하지 않은 상태라면
        if participant not in self.participants:
            await interaction.response.send_message(
                f"{participant.mention} 소환사님은 아직 참가하지 않았습니다-",
                ephemeral=True
            )
            return

        self.participants.remove(participant)
        await interaction.response.edit_message(
            embed = self.embed_collection.내전모집Embed(
                owner=self.owner,
                participants=self.participants,
                시작시간=self.시작시간,
            ),
        )

    # '모집취소' 버튼
    @discord.ui.button(label='⛔ 내전취소', style=discord.ButtonStyle.red, custom_id='cancel')
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        if user == self.owner:
            # 모집 취소 처리 코드
            if self.bot.current_recruitment_message is not None:
                await self.bot.current_recruitment_message.delete()
                self.bot.current_recruitment_message = None
            self.bot.current_participants = []
            self.participants = []  # 참가자 목록 초기화

            # 새로운 임베드 생성
            embed = discord.Embed(
                title="내전 모집이 취소되었습니다-",
                description="",
                color=discord.Color.red()
            )
            # 메시지 수정
            await interaction.response.edit_message(embed=embed, view=None)  # 버튼을 비활성화합니다.
        else:
            await interaction.response.send_message("내전 모집을 시작한 소환사만 취소할 수 있습니다-", ephemeral=True)
       

async def setup(bot):
    await bot.add_cog(내전모집(bot))