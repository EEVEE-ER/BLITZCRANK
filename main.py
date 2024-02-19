import discord
from discord.ext import commands
from common import const

class root(commands.Bot): # 디스코드 개발자 포럼에서 'Privileged Gateway Intents' 항목 All ON
    def __init__(self):
        super().__init__(
            command_prefix=const.PREFIX,
            intents=discord.Intents.all(),
            sync_command=True,
        )

        self.initial_extension = [  # [확장기능] 유지보수 용이하게 요약관리 / extension 폴더 내부에 *.py 파일로 별도 관리
            'extension.내전모집'            
        ]

    async def setup_hook(self):
        for ext in self.initial_extension:
            await self.load_extension(ext)

        await bot.tree.sync()

    async def on_ready(self): # 봇을 실행할때, 터미널에 표시되는 정보
        print(f"================================================= {self.user} ========================================================")
        print(f"================================================= Version : 1.0.0 ========================================================")
        print(f"============================================ \"시스템 가동. 준비 완료\" ====================================================")

        activity = discord.Game("PILTOVER 서버 관리") # 봇 실행시 상태메세지
        await self.change_presence(status=discord.Status.online, activity=activity)

if __name__ == '__main__':
    bot = root()
    bot.run(const.TOKEN) # from common import const 모듈로 common 폴더 안에 있는 const.py 불러오기, const.py 내부에 token으로 토큰 지정