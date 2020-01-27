import re

class MagicCutter:
  def __init__(self, word = None, text = None):
    self.__text = text
    self.__word = self.find_word(word)
    self.__phrases = self.find_phrases()

  def text(self):
    return self.__text

  def word(self):
    return self.__word.group
  
  def phrases(self):
    return self.__phrases

  def find_word(self, word):
    return re.search(word, self.__text)

  def find_phrases(self):
    phrases = []
    splitted_phrases = re.compile('[A-Z]?.*?\.').finditer(self.text)

    for phrase in splitted_phrases:
      if(
        phrase.span()[0] <= self.__word.span()[0] and
        phrase.span()[1] >= self.__word.span()[1]
      ):
        phrases.append(phrase.group())
        
    return phrases

  def title(self):
    pass

  def matter(self):
    pass

  def what_text_say(self):
    pass