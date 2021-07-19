from abc import ABC, abstractmethod

class Field:
  def __init__(self, name, is_required, default_value = None):
      self.name = name
      self.is_required = is_required
      self.default_value = default_value

class Param:
  def __init__(self, fields):
      self.fields = fields
  
  def validate(self, values):
    """做了必传参数的校验"""
    for field in self.fields:
      if field.is_required:
        if not field.name in values:
          raise Exception('%s is required' % field.name)
  

  def merge(self, values):
    """如果某个字段不是必填项，且设定了默认值。那么当传入参数不包含该值时，将默认值设置到values数组当中"""
    for field in self.fields:
      if not field.is_required and field.default_value:
        if not field.name in values:
          values[field.name] = field.default_value

class PreProcessor(ABC):
  def pre_process(self, y, params):
    exp = self.input_spec()
    exp.validate(params)
    exp.merge(params)
    self.do_pre_process(y, **params)
  
  @abstractmethod
  def input_spec(self):
    pass

  @abstractmethod
  def do_pre_process(self, y, params):
    pass

