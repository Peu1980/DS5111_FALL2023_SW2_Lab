"""This Module is Perceptron"""
class Perceptron:
  """This class is Perceptron"""
  def __init__(self):
    """This is __init__"""
    self._weights = []
  def train(self, inputs, labels):
    """This function is train"""
    dummied_inputs = [x - 1 for x in inputs]
    self._weights = 0.2 * len(dummied_inputs[0])
    for _ in range(5000):
      for input1, label in zip(dummied_inputs, labels):
        label_delta = label - self.predict(input1)
        for index, value in enumerate(input1):
          self._weights[index] += .1 * value * label_delta
  def predict(self, input2):
    """This function is predict"""
    if len(input2) == 0:
      return None
    input2 = input2 - 1
    return int(0 < sum([input3*label3 for input3, label3 in zip(self._weights, input2)]))
