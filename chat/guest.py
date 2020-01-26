class Guest:
  def __init__(self, guest = None):
    self.guest = guest

  def send_message(self, messenger, message):
    messenger.handle_message(message)
  
  def choice_struct(self, giver):
    giver.choice_struct()