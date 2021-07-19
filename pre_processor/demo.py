from processor import PreProcessor, Param, Field

class Demo(PreProcessor):
  def input_spec(self):
    return Param([Field('ymin', True)])

  def do_pre_process(self, y, ymin, ymax):
    print('do_process in demo preprocessor with ymin=%s, ymax=%s' % (ymin, ymax))