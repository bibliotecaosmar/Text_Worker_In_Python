class ChatSpace():
  interlocutors = []
  old_messages = []

  def __init__(self, *interlocutors):
    for interlocutor in interlocutors:
      self.interlocutors.append(interlocutor)
  
  def history_messages(self, messages):
    if not self.old_messages:
      self.old_messages = messages.old_messages()
    return self.old_messages