from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import pandas as pd
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from rasa_core.events import AllSlotsReset
from rasa_core.events import Restarted

from rasa_core.actions.forms import (
    BooleanFormField,
    EntityFormField,
    FormAction,
    FreeTextFormField
)

class GetAllSearchResults(FormAction):
	RANDOMIZE = False
	@staticmethod
	def required_fields():
		return [
		EntityFormField("location", "location"),
		EntityFormField("cuisine", "cuisine"),
		EntityFormField("price", "price")
		]
		
	def name(self):
		return 'get_all_search_results'
		
	def submit(self, dispatcher, tracker, domain):
		config={ "user_key":"2ee4b992c32c9d3fba974f2345ceb640"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price_range = tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'mexican':73,'chinese':25,'italian':55,'american':1,'north indian':50,'south indian':85}
		dispatcher.utter_message("Hold on while we fetch the restaurants ..............")
		fetchIndex=0
		search_results = pd.DataFrame(columns=['Restaurant Name','Restaurant locality address','Average budget for two people','Zomato user rating'])
		while (fetchIndex!=80):
			results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20,fetchIndex)
			d = json.loads(results)
			response=""
			if d['results_found'] == 0:
				break
			else:
				for restaurant in d['restaurants']:
					search_results = search_results.append({'Restaurant Name':restaurant['restaurant']['name'],
															'Restaurant locality address': restaurant['restaurant']['location']['address'],
															'Average budget for two people':restaurant['restaurant']['average_cost_for_two'],
															'Zomato user rating':restaurant['restaurant']['user_rating']['aggregate_rating']},ignore_index=True)

			fetchIndex = fetchIndex+20
		if(len(search_results)==0):
			dispatcher.utter_template("utter_no_restaurants_found")
			SlotSet("price", None)
			return[SlotSet("cuisine", None)]
		#response= "no results"
		else:
			return[SlotSet("full_restaurant_search",search_results.to_json())]
			
			
class ActionSearchRestaurants(Action):

	def name(self):
		return 'action_restaurant'

	def run(self, dispatcher, tracker, domain):
		response=""
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price_range = tracker.get_slot('price')
		search_results = pd.read_json(tracker.get_slot('full_restaurant_search'))

		if(price_range=="1"):
			filterd_results = search_results[search_results['Average budget for two people'] <=300]
			filterd_results.sort_values('Zomato user rating',ascending=False,inplace=True)
			if(len(filterd_results)==0):
				SlotSet("price", None)
				dispatcher.utter_template("utter_no_match_price_range", tracker)
				return[SlotSet("query_restaurant_search", None)]
				#response=response+" Sorry couldn't find any restaurants in price range. Please re enter different price range "
			else:
				for index, row in filterd_results.head(5).iterrows():
					response = response+row['Restaurant Name']+" in "+ row['Restaurant locality address']+" has been rated "+str(row['Zomato user rating'])+"\n"
				return[SlotSet("query_restaurant_search", response)]
		elif(price_range=="2"):
			filterd_results = search_results[(search_results['Average budget for two people'] > 300) &  (search_results['Average budget for two people'] <= 700)]
			filterd_results.sort_values('Zomato user rating',ascending=False,inplace=True)
			if(len(filterd_results)==0):
				SlotSet("price", None)
				dispatcher.utter_template("utter_no_match_price_range", tracker)
				return[SlotSet("query_restaurant_search", None)]
			else:
				for index, row in filterd_results.head(5).iterrows():
					response = response+row['Restaurant Name']+" in "+ row['Restaurant locality address']+" has been rated "+str(row['Zomato user rating'])+"\n"
				return[SlotSet("query_restaurant_search", response)]
		elif(price_range=="3"):				
			filterd_results = search_results[search_results['Average budget for two people'] >700]
			filterd_results.sort_values('Zomato user rating',ascending=False,inplace=True)
			if(len(filterd_results)==0):
				#response=response+" Sorry couldn't find any restaurants in price range. Please re enter different price range "
				SlotSet("price", None)
				dispatcher.utter_template("utter_no_match_price_range", tracker)
				return[SlotSet("query_restaurant_search", None)]
			else:
				for index, row in filterd_results.head(5).iterrows():
					response = response+row['Restaurant Name']+" in "+ row['Restaurant locality address']+" has been rated "+str(row['Zomato user rating'])+"\n"	
				return[SlotSet("query_restaurant_search", response)]

class ActionValidateLocation(Action):
	def name(self):
		return 'validate_location'
		
	def run(self, dispatcher, tracker, domain):
		city_list = ['ahmedabad', 'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune',
					'agra', 'ajmer', 'aligarh', 'allahabad', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 
					'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city', 'chandigarh', 'coimbatore', 
					 'cuttack', 'dehradun', 'dhanbad', 'durg-bhilai nagar', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 
					 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon', 'guwahati', 'gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 
					 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur', 'kanpur', 'kakinada', 'kochi', 'kottayam', 
					 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 'madurai', 'malappuram', 'mathura', 'goa', 
					 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 
					 'pondicherry', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 
					 'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirunelveli', 'tiruppur', 
					 'ujjain', 'vijayapura', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 'visakhapatnam', 'warangal']
		loc = tracker.get_slot('location')
		response = ""
		if(loc == None):
			dispatcher.utter_template("utter_invalid_location",tracker)
			return [SlotSet('location',None)]
		elif(loc.lower() not in city_list):
			dispatcher.utter_template("utter_invalid_location",tracker)
			return [SlotSet('location',None)]
		else:
			return [SlotSet('location',loc)]

class ActionValidateCuisine(Action):
	def name(self):
		return 'validate_cuisine'
	
	def run(self, dispatcher, tracker, domain):
		cuisines=['mexican','chinese','italian','american','north indian','south indian']
		cuisine = tracker.get_slot('cuisine')
		#response = ""
		if(cuisine == None):
			dispatcher.utter_template("utter_invalid_cuisine",tracker)
			return [SlotSet('cuisine',None)]
		elif(cuisine.lower() not in cuisines):
			dispatcher.utter_template("utter_invalid_cuisine",tracker)
			return [SlotSet('cuisine',None)]
		else:
			return [SlotSet('cuisine',cuisine)]

import re
class ActionSendEmail(Action):
	def name(self):
		return 'action_email'
		
	def run(self, dispatcher, tracker, domain):
		price_range = tracker.get_slot('price')
		email = tracker.get_slot('email')
		if(email==None):
			dispatcher.utter_template("utter_email_not_recognized", tracker)
			return[SlotSet('email',None)]
			
		list_email = re.findall('([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)',email) 
		
		msg = MIMEMultipart('alternative')
		
		search_results = pd.read_json(tracker.get_slot('full_restaurant_search'))
		if(len(list_email)==0):
			dispatcher.utter_template("utter_email_not_recognized", tracker)
			return[SlotSet('email',email)]
		elif(len(search_results)==0):
			msg.attach(MIMEText("Sorry no results found",'html'))
		else:
			email = list_email[0]
			if(price_range=="1"):
				filterd_results = search_results[search_results['Average budget for two people'] <=300]
				filterd_results.sort_values('Zomato user rating',ascending=False,inplace=True)
				if(len(filterd_results)==0):
					msg.attach(MIMEText("Sorry couldn't find any restaurants in price range. Please choose different price range",'html'))
				else:
					msg.attach(MIMEText(filterd_results.head(10).to_html(),'html'))
			elif(price_range=="2"):
				filterd_results = search_results[(search_results['Average budget for two people'] > 300) &  (search_results['Average budget for two people'] <= 700)]
				filterd_results.sort_values('Zomato user rating',ascending=False,inplace=True)
				if(len(filterd_results)==0):
					msg.attach(MIMEText("Sorry couldn't find any restaurants in price range. Please choose different price range",'html'))
				else:
					msg.attach(MIMEText(filterd_results.head(10).to_html(),'html'))
			elif(price_range=="3"):				
				filterd_results = search_results[search_results['Average budget for two people'] >700]
				filterd_results.sort_values('Zomato user rating',ascending=False,inplace=True)
				if(len(filterd_results)==0):
					msg.attach(MIMEText("Sorry couldn't find any restaurants in price range. Please choose different price range",'html'))
				else:
					msg.attach(MIMEText(filterd_results.head(10).to_html(),'html'))

		msg['Subject'] = 'Restaurant search results from Zomato'
		msg['From'] = 'botzomato@gmail.com'
		msg['To'] = email

			# Send the message via our own SMTP server.

			#server = smtplib.SMTP('smtp.gmail.com:587')
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
			#server.starttls()
		server.login('botzomato@gmail.com','IIITBtest2018')
		server.send_message(msg)
		server.quit()
		
		dispatcher.utter_template("utter_email_sent_successfully", tracker)
		return[SlotSet('email',email)]

		
class ActionValidatePrice(Action):
	def name(self):
		return 'validate_price'
	
	def run(self, dispatcher, tracker, domain):
		prices=['1','2','3']
		price = tracker.get_slot('price')
		#response = ""
		if(price == None):
			dispatcher.utter_template("utter_invalid_price_range",tracker)
			return [SlotSet('price',None)]
		elif(price.lower() not in prices):
			dispatcher.utter_template("utter_invalid_price_range",tracker)
			return [SlotSet('price',None)]
		else:
			return [SlotSet('price',price)]
			
class ActionGoodBye(Action):
	def name(self):
		return 'action_bye'
		
	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_template("utter_goodbye",tracker)
		return[AllSlotsReset()]
			
class ActionRestarted(Action): 	
    def name(self): 		
        return 'action_restarted' 	
    def run(self, dispatcher, tracker, domain): 
        return[Restarted()]
		
class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]