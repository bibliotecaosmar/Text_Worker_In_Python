class Word:
  """
  Collect and storage word information about context.
  """
  
  def __init__(self, word, line, order):
    """
    Start the instance of classe with the parameters: word, line and order.
    """
    
    self.word = word
    self.line = line
    self.order = order  

  def context(self, magiccutter):
    """
    Create a serial of informations about the particular word in the text.
    """
    magiccutter.find(self.word, self.line, self.order)

    self.phrase = magiccutter.phrase()
    self.text_title = magiccutter.title()
    self.matter = magiccutter.matter()
    self.what_text_say = magiccutter.what_text_say()
