from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
#from rasa_slack_connector import SlackInput
from rasa_core.channels.slack import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

#input_channel = SlackInput('xoxp-412623938595-413793902855-412450660912-a9ef5225c24fae9eefa57db2a2b537a7', #app verification token
#							'xoxb-412623938595-413934206631-HRkw5NPTvnzkcq1tNcycrOA6', # bot verification token
#							'aeMa8f0hOBtDbuR0aPQMTBac', # slack verification token
#							True)

input_channel = SlackInput(slack_token='xoxb-412623938595-413934206631-HRkw5NPTvnzkcq1tNcycrOA6')

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))