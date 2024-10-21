import nonebot
from nonebot.adapters.onebot.v11 import Adapter
import os
from bot import instance_bot


nonebot.bot_home = os.path.dirname(__file__)
# 初始化 NoneBot
nonebot.init()

# 注册适配器
driver = nonebot.get_driver()
driver.register_adapter(Adapter)
driver.on_bot_connect(instance_bot)

# 在这里加载插件
nonebot.load_builtin_plugins('echo')
nonebot.load_plugins('plugins')


if __name__ == '__main__':
  nonebot.run()
