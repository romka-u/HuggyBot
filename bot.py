# -*- coding: utf-8 -*-

import random
from collections import defaultdict

import interaction
from topics import ALL_TOPICS


POSITIVES = [u"да-да", u"ага", u"*yes-yes*", u"*nod*"]
HUG_IS_BETTER = [u"лучше *hug* же, а не ", u"(hug) лучше, чем ", u"нужно делать (hug), а не "]


class HuggyBot(object):
    def __init__(self):
        self.last_update_id = 0
        self.topic = None
        self.names = defaultdict(list)

    def process_updates(self):
        updates = interaction.get_updates(self.last_update_id + 1)
        messages = []
        for update in updates:
            if update.update_id > self.last_update_id:
                self.last_update_id = update.update_id
                messages.append(update.message)

        for message in messages:
            try:
                print "process", message.text
                self.process_message(message)
            except Exception, e:
                print e
                interaction.send_message(message.chat_id, u"Я сломался :(")

    def process_message(self, message):
        if self.topic is None:
            self.topic = self.define_topic(message)
            if self.topic is None:
                self.default_answer(message)
        elif self.topic is not None:
            if self.topic.accept_message(message):
                return
            else:
                self.topic = None
                self.default_answer(message)

    def default_answer(self, message):
        if "hug" in message.text:
            interaction.send_message(message.chat_id,
                random.choice(POSITIVES) + ", " +
                random.choice(self.names[message.sender.id]) + ", " + message.text)
        else:
            interaction.send_message(message.chat_id,
                random.choice(self.names[message.sender.id]) + "! " +
                random.choice(HUG_IS_BETTER) + message.text)

    def define_topic(self, message):
        for Topic in ALL_TOPICS:
            if Topic.can_be_started_with(message):
                return Topic(self, message)

        return None
