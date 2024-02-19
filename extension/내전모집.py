import discord
from discord.ext import commands
from discord import app_commands
from typing import List
from common.EmbedCollection import EmbedCollection
from common.Button import ButtonCollection

내전최대인원 : int = 1 #내전인원은 10명이 되어야 하는데, 우선 테스트로 2로 해놓음

class 내전모집(commands.Cog): # /내전모집 커멘드 클래스
    def __init__(self, bot):
        self.bot = bot
        self.arstarstarst.current_participants = []
        self.embed_collection = EmbedCollection()
        
        
    @app_commands.command(name="내전모집", description="내전을 모집합니다-")  # '/내전모집' 커멘드
    @app_commands.describe(시작시간="'즉시 또는 PM 12시'와 같이 입력하세요-")
    async def 내전모집(self, interaction: discord.Interaction, 시작시간: str):
        user = interaction.user
        
        # 임베드 관련 부분
        embed = self.embed_collection.내전모집임베드(
            participants=[],
            owner = user,
            시작시간 = 시작시간
        )
        view = ButtonCollection(
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


async def setup(bot):
    await bot.add_cog(내전모집(bot))