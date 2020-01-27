import re

class MagicCutter:
  phrases = []

  def __init__(self, text):
    self.text = text

  def find(self, word):
    self.word = re.search(word, self.text)

  def phrase(self):
    splitted_phrases = re.compile('[A-Z]?.*?\.').finditer(self.text)

    for phrase in splitted_phrases:
      if(
        phrase.span()[0] <= self.word.span()[0] and
        phrase.span()[1] >= self.word.span()[1]
      ):
        self.phrases.append(phrase.group()) 

  def title(self):
    pass

  def matter(self):
    pass

  def what_text_say(self):
    pass