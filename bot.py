from nonebot.adapters import Bot, Event, Message
from typing import Sequence
from functools import partial


async def send_forward_msg(
  bot: Bot,
  event: Event = None,
  to_group: bool = True,
  messages: Sequence = None,
  name: str = '',
  uin: str = '',
):
  if not name:
    name = '小派魔'
  if not uin:
    uin = bot.self_id

  def to_json(msg: Message):
    return {'type': 'node', 'data': {'name': name, 'uin': uin, 'content': msg}}

  messages = [to_json(m) for m in messages]
  if to_group:
    return await bot.call_api(
      'send_group_forward_msg', group_id=str(event.group_id), messages=messages
    )
  return await bot.call_api(
    'send_private_forward_msg', user_id=str(event.user_id), messages=messages
  )


async def send_group_forward_msg(
  bot: Bot,
  group_id: str,
  messages: Sequence,
  name: str = '',
  uin: str = '',
):
  return await bot.send_forward_msg(
    type('Event', (), {'group_id': group_id}), True, messages, name, uin
  )


async def send_private_forward_msg(
  bot: Bot,
  user_id: str,
  messages: Sequence,
  name: str = '',
  uin: str = '',
):
  return await bot.send_forward_msg(
    type('Event', (), {'user_id': user_id}), True, messages, name, uin
  )


def instance_bot(bot: Bot):
  bot.send_forward_msg = partial(send_forward_msg, bot)
  bot.send_group_forward_msg = partial(send_group_forward_msg, bot)
  bot.send_private_forward_msg = partial(send_private_forward_msg, bot)
