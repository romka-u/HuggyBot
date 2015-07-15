# -*- coding: utf-8 -*-

import random

from interaction import send_message
from semantic import is_negative


GREETING = u"Привет! Я HuggyBot :) А как я могу тебя называть?"
NEXT = [
    u"Окей. А ещё?",
    u"Ага. Как-нибудь ещё?",
    u"Очень приятно. Другие варианты?"
]

PREFIXES = [
    u"ещё ",
    u"можно ",
    u"просто ",
    u"например ",
    u"например, ",
]


class WelcomeTopic(object):
    def __init__(self, bot, first_message):
        self.bot = bot
        send_message(first_message.chat_id, GREETING)
        self.state = "WAITING"

    def accept_message(self, message):
        if self.state == "FINISHED":
            return False

        if is_negative(message.text):
            if self.bot.names[message.sender.id]:
                send_message(message.chat_id, u"Хорошо, будешь " + u", ".join(self.bot.names[message.sender.id]))
                self.state = "FINISHED"
            else:
                send_message(message.chat_id, u"Но надо же как-то называть!")
        elif "?" in message.text:
            send_message(message.chat_id, u"Ты скажи, можно ли тебя как-то ещё называть, а потом будешь вопросы задавать :)")
            send_message(message.chat_id, u"Если никак больше нельзя, так и скажи :)")
        else:
            name = message.text
            while True:
                for prefix in PREFIXES:
                    if name.lower().startswith(prefix):
                        name = name[len(prefix):]
                        break
                else:
                    break
            self.bot.names[message.sender.id].append(name)
            send_message(message.chat_id, random.choice(NEXT))

        return True

    @staticmethod
    def can_be_started_with(message):
        return message.text.startswith("/start")
