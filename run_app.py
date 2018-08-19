from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput
#from rasa_core.channels.slack import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-412623938595-413793902855-416392787079-ede4781c414d804788e6321f1ef04979', #app verification token
							'xoxb-412623938595-413934206631-8YxnNnkgth6fouCemve8920S', # bot verification token
							'aeMa8f0hOBtDbuR0aPQMTBac', # slack verification token
							True)

#input_channel = SlackInput(slack_token='xoxp-412623938595-413793902855-416392787079-ede4781c414d804788e6321f1ef04979')

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))