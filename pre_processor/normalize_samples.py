from processor import PreProcessor, Param, Field

class NormalizeSamples(PreProcessor):
  def input_spec(self):
    return Param([Field('sr', True), Field('second', False, 9 * 60)])

  def do_pre_process(self, y, params):
    """
    统一采样数，音频长度也统一, 默认是采样9m的样本数
    Parameters
    ----------
    y: np.ndarray[shape = (n,)] or None
                (optional) audio time series.
    Returns
    ----------

    """
    if params['second'] is None:
        return y
    else:
        # return y[0:sr * second]
        return y[len(y) - params['sr'] * params['second']:]  # 从原始音频后段取样本，通常开头几个样本值都是0，会失帧
        # return y[sr*3:sr*(3+second)]  #从第三秒的样本开始采样，到第6秒采样结束， 一共3秒的采样数