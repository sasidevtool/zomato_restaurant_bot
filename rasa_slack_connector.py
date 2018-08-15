from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from builtins import str
from flask import Blueprint, request, jsonify

from rasa_core.channels.channel import UserMessage, OutputChannel
from rasa_core.channels.rest import HttpInputComponent

logger = logging.getLogger(__name__)


class SlackBot(OutputChannel):
	def __init__(self, slack_verification_token, channel):
		self.slack_verification_token = slack_verification_token
		self.channel = channel
		
	def send_text_message(self, recipient_id, message):
		from slackclient import SlackClient
		text = message
		recipient = recipient_id
		
		CLIENT = SlackClient(self.slack_verification_token)
		CLIENT.api_call('chat.postMessage', channel = self.channel, text = text, as_user = True)
		




class SlackInput(HttpInputComponent):

	def __init__(self, slack_dev_token, slack_verification_token, slack_client, debug_mode):
		self.slack_dev_token = slack_dev_token
		self.debug_mode = debug_mode
		self.slack_client = slack_client
		self.slack_verification_token = slack_verification_token
		
		
	def __init__(self, slack_dev_token, slack_verification_token, slack_client, debug_mode, errors_ignore_retry=None):
		self.slack_dev_token = slack_dev_token
		self.debug_mode = debug_mode
		self.slack_client = slack_client
		self.slack_verification_token = slack_verification_token
		self.errors_ignore_retry = errors_ignore_retry or ('http_timeout',)
		
		 
	def blueprint(self, on_new_message):
		from flask import Flask, request, Response
		slack_webhook = Blueprint('slack_webhook', __name__)
		
		@slack_webhook.route('/', methods = ['GET'])
		def health():
			return jsonify({'status':'ok'})
			
		@slack_webhook.route('/slack/events', methods = ['POST'])
		def event():
			if request.json.get('type') == 'url_verification':
				return request.json.get('challenge'), 200
				
			if request.json.get('token') == self.slack_client and request.json.get('type') == 'event_callback':
				data = request.json
				messaging_events = data.get('event')
				channel = messaging_events.get('channel')
				user = messaging_events.get('user')
				text = messaging_events.get('text')
				bot = messaging_events.get('bot_id')
				retry_reason = request.headers.environ.get('HTTP_X_SLACK_RETRY_REASON')
				retry_count = request.headers.environ.get('HTTP_X_SLACK_RETRY_NUM')
				if retry_count and retry_reason in self.errors_ignore_retry:
					logger.warning("Received retry #{} request from slack"
                           " due to {}".format(retry_count, retry_reason))
					return Response(status=201, headers={'X-Slack-No-Retry': 1})
				if bot == None:
					on_new_message(UserMessage(text, SlackBot(self.slack_verification_token, channel)))
					
			return Response(headers={'X-Slack-No-Retry': 1}), 200
			
		return slack_webhook
				
		
		
		
		
