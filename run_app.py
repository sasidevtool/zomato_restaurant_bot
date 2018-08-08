from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-412623938595-413793902855-413037515701-328f4006c535f5897aad8441a0d3191a', #app verification token
							'xoxb-412623938595-413934206631-N6niASrXfDqugc6kovka0WoI', # bot verification token
							'aeMa8f0hOBtDbuR0aPQMTBac', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))