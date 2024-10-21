import random
import hashlib
from typing import Union


def randStr(length: int = 8) -> str:
  """
  随机字符串

  Args:
    length: 字符串长度, 默认为 8

  Returns:
    str: 字符串
  """
  chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  res = ''
  for i in range(length):
    res += random.choice(chars)
  return res


def md5sum(s: Union[str, bytes] = None) -> str:
  """
  计算字符串的 md5 值
  """
  if isinstance(s, bytes):
    return hashlib.md5(s).hexdigest()
  return hashlib.md5(s.encode()).hexdigest()
