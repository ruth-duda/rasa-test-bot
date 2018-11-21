from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionOrderProduct(Action):
	def name(self):
		return 'action_order_product'

	def run(self, dispatcher, tracker, domain):
    
		router = tracker.get_slot('router')
		confirmationNumber = 123456 #later generate through some process

		response = """Your product {} is ordered for you. It will be shipped to your address. Your confirmation number is {}""".format(router, confirmationNumber)

		dispatcher.utter_message(response)
		return [SlotSet('router',router)]