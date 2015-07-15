# -*- coding: utf-8 -*-

import random

import interaction


POSITIVES = [u"да-да", u"ага", u"*yes-yes*", u"*nod*"]
HUG_IS_BETTER = [u"лучше *hug* же, а не ", u"(hug) лучше, чем ", u"нужно делать (hug), а не "]


class HuggyBot(object):
    def __init__(self):
        self.last_update_id = 0

    def process_updates(self):
        updates = interaction.get_updates(self.last_update_id + 1)
        messages = []
        for update in updates:
            if update.update_id > self.last_update_id:
                self.last_update_id = update.update_id
                messages.append(update.message)

        for message in messages:
            if "hug" in message.text:
                interaction.send_message(message.chat_id,
                    random.choice(POSITIVES) + ", " + message.text)
            else:
                interaction.send_message(message.chat_id,
                    random.choice(HUG_IS_BETTER) + message.text)
