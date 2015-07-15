

class User(object):
    """ https://core.telegram.org/bots/api#user """
    def __init__(self, user):
        self.id = user["id"]
        self.first_name = user["first_name"]

        if "last_name" in user:
            self.last_name = user["last_name"]
        else:
            self.last_name = None

        if "username" in user:
            self.username = user["username"]
        else:
            self.username = None


class Message(object):
    """ https://core.telegram.org/bots/api#message """
    def __init__(self, message):
        self.message_id = message["message_id"]
        self.sender = User(message["from"])  # can not use self.from in python
        self.date = int(message["date"])
        self.chat_id = message["chat"]["id"]

        self.text = message["text"] if "text" in message else ""


class Update(object):
    """ https://core.telegram.org/bots/api#update """
    def __init__(self, update):
        self.update_id = int(update["update_id"])
        self.message = Message(update["message"])
