import json
import os.path
from .file import getDataFile


def getData(file: str) -> dict:
  path = getDataFile(f'{file}.json')
  if not os.path.isfile(path):
    setData(file, dict())
  with open(path, 'r') as f:
    data = f.read()
    if data == '':
      return {}
    data = json.loads(data)
    return data


def setData(file: str, data: dict):
  with open(getDataFile(f'{file}.json'), 'w') as f:
    f.write(json.dumps(data, indent=4))


class Data(object):
  class Unset:
    pass

  unset = Unset()

  def __new__(cls, *args, **kwargs):
    if not hasattr(cls, '__instance'):
      cls.__instance = super().__new__(cls)
    return cls.__instance

  def __init__(self, file: str):
    self.file = file
    self.data = getData(file)

  def __repr__(self):
    return f'Data(file={self.file}, data={self.data})'

  def __contains__(self, key):
    return key in self.data

  def __len__(self):
    return len(self.data)

  @staticmethod
  def value_to_json(v):
    return v

  @staticmethod
  def value_de_json(v):
    return v

  def __getitem__(self, key, default=unset):
    if isinstance(default, Data.Unset):
      v = self.data.get(str(key))
    else:
      v = self.data.get(str(key), default)
    return self.value_de_json(v)

  def __setitem__(self, key, value):
    self.data[str(key)] = self.value_to_json(value)

  def __delitem__(self, key):
    self.data.pop(key)

  def get(self, key, default=unset):
    if isinstance(default, Data.Unset):
      return self.__getitem__(key)
    return self.__getitem__(key, default)

  def setdefault(self, key, default=None):
    if key in self.data:
      return self.__getitem__(key)
    self.__setitem__(key, default)
    return default

  def keys(self):
    return self.data.keys()

  def items(self):
    return self.data.items()

  def values(self):
    return self.data.values()

  def save(self):
    setData(self.file, self.data)

  def close(self):
    setData(self.file, self.data)

  def __enter__(self):
    return self

  def __exit__(self, type, value, trace):
    self.save()

  def __iter__(self):
    return iter(self.data)


class Settings(Data):
  def __init__(self):
    super().__init__('settings')
