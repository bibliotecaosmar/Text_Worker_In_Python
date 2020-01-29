import re

class MagicCutter:
  """
  Tool to use select text elements to use in data science.
  """
  def __init__(self, text = None, word = None):
    self.__text = text
    self.__word = self.find_word(word)

  def find_word(self, word):
    return re.search(word, self.__text)

  def find_phrases(self):
    """
    List all phrases of the a text.
    """
    phrases = []
    splitted_phrases = re.compile('[A-Z]?.*?\.').finditer(self.__text)

    for phrase in splitted_phrases:
      if(
        phrase.span()[0] <= self.__word.span()[0] and
        phrase.span()[1] >= self.__word.span()[1]
      ):
        phrases.append(phrase.group())
        
    return phrases

  def find_title(self):
    """
    Return probable title string.
    """
    return re.compile('[A-Z]?.*?\.').findall(self.__text)[0]

  def discover_matter(self):
    pass

  def what_text_say(self):
    pass