import requests
import json
import os


# curl -X GET --header "Accept: application/json" 
#             --header "user-key: 0292ccbf972bcfe2cdfdd27aa92637ff" 
#  "https://developers.zomato.com/api/v2.1/search?
#                                          entity_id=5&
#                                          entity_type=city&
#                                          start=20&
#                                          cuisines=102"

TOTAL_PUNE_RESTAURANTS = 9648
PUNE_CITY_ID = 5
API_KEY_FOR_THE_DAY = "0292ccbf972bcfe2cdfdd27aa92637ff"

CUISINES = [
	{"cuisine_id": 25, "cuisine_name": "Chinese"},
	{"cuisine_id": 73, "cuisine_name": "Mexican"},
	{"cuisine_id": 55, "cuisine_name": "Italian"},
	{"cuisine_id": 1,  "cuisine_name": "American"},
	{"cuisine_id": 85, "cuisine_name": "South Indian"},
	{"cuisine_id": 50, "cuisine_name": "North Indian"}]

CITIES = ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 
          'Mumbai', 'Pune', 'Agra', 'Ajmer', 'Aligarh', 'Allahabad', 'Amravati',
          'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar',
          'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bokaro Steel City',
          'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad',
          'Durg-Bhilai Nagar', 'Durgapur', 'Erode', 'Faridabad', 'Firozabad',
          'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gurgaon', 
          'Guwahati‚ Gwalior', 'Hubli-Dharwad', 'Indore', 'Jabalpur', 
          'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 
          'Jodhpur', 'Kannur', 'Kanpur', 'Kakinada', 'Kochi', 'Kottayam', 
          'Kolhapur', 'Kollam', 'Kota', 'Kozhikode', 'Kurnool', 'Lucknow', 
          'Ludhiana', 'Madurai', 'Malappuram', 'Mathura', 'Goa', 'Mangalore',
          'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 
          'Nellore', 'Noida', 'Palakkad', 'Patna', 'Pondicherry', 'Raipur', 
          'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 
          'Siliguri', 'Solapur', 'Srinagar', 'Sultanpur', 'Surat', 
          'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 
          'Tiruppur', 'Ujjain', 'Vijayapura', 'Vadodara', 'Varanasi', 
          'Vasai-Virar City', 'Vijayawada', 'Visakhapatnam', 'Warangal']

def search_restaurants(start=0, cuisine_id=None, city_id=None):
	payload = {"entity_id": city_id,
	           "entity_type": "city",
	           "cuisines":cuisine_id,
	           "start": start}
	headers = {"Accept": "application/json",
	           "user-key": API_KEY_FOR_THE_DAY}
	req = requests.get("https://developers.zomato.com/api/v2.1/search", 
		               params=payload,
		               headers=headers)
	return req.json()

def get_city_id(city_name):
	payload = {"query": city_name}
	headers = {"Accept": "application/json",
	           "user-key": API_KEY_FOR_THE_DAY}
	req = requests.get("https://developers.zomato.com/api/v2.1/locations", 
		               params=payload,
		               headers=headers)
	return [{"city_name": loc["city_name"],
	         "city_id": loc["city_id"]} 
	        for loc in req.json()["location_suggestions"]]


def collect_all_restaurants(cuisine_id, city_id):
	start = 0
	restaurants = []
	# api returns 20 elems each fetch
	while start < 100:
		search_data = search_restaurants(start, cuisine_id, city_id)
		restaurants += search_data["restaurants"]
		count_restaurants = len(search_data["restaurants"])
		print("Got {} restaurants".format(count_restaurants))
		start += count_restaurants
		print("Setting start at: {}".format(start))
		if count_restaurants == 0:
			# API throttled
			break

	return restaurants

def get_all_cuisine_ids():
	return json.load(open("pune_cuisines.json", "r"))["cuisines"]

def save_cuisine(cuisine, city_meta):
	cuisine_restaurants = collect_all_restaurants(
		cuisine["cuisine_id"], city_meta["city_id"])
	filename = "cuisines/{}_restuarants_{}.json".format(
			city_meta["city_name"], cuisine["cuisine_name"])
	print("Saving {} at {}".format(len(cuisine_restaurants), filename))
	open(filename, "w").write(json.dumps(cuisine_restaurants))

def get_all_cuisines():
	all_cuisines = get_all_cuisine_ids()
	print("Found {} cuisines in Pune".format(len(all_cuisines)))
	for i, cuisine in enumerate(all_cuisines):
		print("-----------------{}:  {}----------------".format(
			i, cuisine["cuisine"]["cuisine_name"]))
		save_cuisine(cuisine["cuisine"])
		print("----------------------------------------------")
	
# ===========================================
# day 1
# -------------------------------------------	
# uncomment following to save all the cuisine 
# restaurants max 100 in each
# -------------------------------------------

# get_all_cuisines()

# -------------------------------------------

def get_all_unique_restuarants(city):
	res_ids = set()
	for restfn in os.listdir("cuisines"):
		restdata = json.load(open("cuisines/{}".format(restfn), "r"))
		res_ids.update([rd["restaurant"]["id"] for rd in restdata])
	print("Found {} unique restaurants".format(len(res_ids)))
	return res_ids

def save_all_restuarants_for(city_name):
	cities = get_city_id(city_name)
	for cmeta in cities:
		for i, cuisine in enumerate(CUISINES):
			print("-----------------{}:  {}----------------".format(
				  i, cuisine["cuisine_name"]))
			save_cuisine(cuisine, cmeta)
			print("----------------------------------------------")

def save_restaurants_for_cities():
	for cityname in CITIES:
		print("=================={}======================".format(cityname))
		save_all_restuarants_for(cityname)
		print("==============================================")

save_restaurants_for_cities()