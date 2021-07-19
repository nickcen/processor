import yaml
import logging
import importlib


class Pipeline:
  def __init__(self) -> None:
      pass
  
  def load_pipeline(self, filepath):
    logging.debug("load config from file [%s]" % filepath)
    with open(filepath) as file:
      self.configs = yaml.load(file, Loader=yaml.FullLoader)

  def run(self):
    stream = self.load_file()
    self.pre_process(stream)
  
  def load_file(self):
    return []

  def pre_process(self, stream):
    if 'pre_processors' in self.configs:
      pre_processors = self.configs['pre_processors']
      for pre_processor in pre_processors:
        logging.debug('load pre_processor [%s]' % pre_processor['name'])

        inst = self.load_pre_processor(pre_processor['name'])
        params = pre_processor.get('params', {})

        inst.pre_process(stream, params)
  
  def load_pre_processor(self, name):
    module_name = 'pre_processor.%s' % name
    class_name = "".join(map(lambda x:x.capitalize(), name.split("_")))
    module = importlib.import_module(module_name)
    class_ = getattr(module, class_name)
    return class_()