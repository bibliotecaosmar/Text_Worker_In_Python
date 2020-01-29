from highlighter_pen.magiccutter import MagicCutter as magiccutter

class Word:
  """
  Collect and storage word information about context.
  """
  
  def __init__(self, word, text):
    """
    Start the instance of classe with the parameters: word, line and order.
    """
    
    self.__word = word
    self.__text = text
    
  def context(self, magiccutter):
    """
    Create a serial of informations about the particular word in the text.
    """

    magiccutter(self.__text, self.__word)

    self.__phrases        = magiccutter.find_phrases()
    self.__text_title     = magiccutter.find_title()
    self.__matter         = magiccutter.discover_matter()
    self.__what_text_say  = magiccutter.what_text_say()

  def text(self):
    return self.__text

  def word(self):
    return self.__word

  def text_title(self):
    return self.__text_title

  def phrases(self):
    return self.__phrases

  def matter(self):
    return self.__matter
  
  def what_text_say(self):
    return self.__what_text_say