from chat.messenger import Messenger as messenger
from chat.giver import Giver as giver

class Guest:
  def __init__(self, guest = None):
    self.__guest = guest

  def send_message(self, messenger, message):
    messenger.handle_message(message, self.__guest)
  
  def choice_struct(self, giver):
    giver.choice_struct().take()