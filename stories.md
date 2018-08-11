## Generated Story 1868904741969810973
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "hyderabad"}
    - validate_location
    - slot{"location": "hyderabad"}
    - validate_cuisine
    - slot{"cuisine": "chinese"}
    - get_all_search_results
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - validate_price
    - slot{"price": "2"}
    - get_all_search_results
    - slot{"price": "2"}
    - slot{"full_restaurant_search": "{\"Restaurant Name\":{\"0\":\"AB's - Absolute Barbecues\",\"1\":\"Chili's American Grill & Bar\",\"2\":\"AB's - Absolute Barbecues\",\"3\":\"Chili's American Grill & Bar\",\"4\":\"Exotica\",\"5\":\"Mekong - Marigold Hotel\",\"6\":\"Flechazo\",\"7\":\"Farzi Cafe\",\"8\":\"Barbeque Pride\",\"9\":\"The Fisherman's Wharf\",\"10\":\"Zero40 Brewing\",\"11\":\"Prost Brew Pub\",\"12\":\"Haiku\",\"13\":\"Tipsy Stories Rooftop Bar\",\"14\":\"Fat Pigeon - Bar Hop\",\"15\":\"Seasonal Tastes - The Westin\",\"16\":\"Flying Spaghetti Monster\",\"17\":\"Tatva\",\"18\":\"Komatose - Holiday Inn Express & Suites\",\"19\":\"The Himalayan Cafe\",\"20\":\"Vapour - Brew Pub\",\"21\":\"Chutneys\",\"22\":\"China Bistro\",\"23\":\"Mamagoto\",\"24\":\"Karachi Bakery\",\"25\":\"Republic Of Noodles - Lemon Tree Premier\",\"26\":\"Mamagoto\",\"27\":\"MOB\",\"28\":\"King And Cardinal Bakery\",\"29\":\"Saffron Mantra\",\"30\":\"Hashi\",\"31\":\"Zega - Sheraton Hyderabad Hotel\",\"32\":\"Over The Moon Brew Company\",\"33\":\"Amnesia Lounge Bar\",\"34\":\"Jonathan's Kitchen - Holiday Inn Express & Suites\",\"35\":\"United Kitchens of India\",\"36\":\"Heart Cup Coffee\",\"37\":\"By The Bottle\",\"38\":\"Kavanah\",\"39\":\"Headquarters\",\"40\":\"Here's What's Cookin'\",\"41\":\"Ci Gusta!\",\"42\":\"WOK Republic\",\"43\":\"Barbeque Nation\",\"44\":\"Paradise\",\"45\":\"Spice 6 - The Global Cuisine\",\"46\":\"Kim Fung\",\"47\":\"Okra - Hyderabad Marriott Hotel & Convention Centre\",\"48\":\"Groove 9\",\"49\":\"Indian Foodies Hub\",\"50\":\"Deccan Pavilion - ITC Kakatiya\",\"51\":\"Talking Hands\",\"52\":\"Republic Of Noodles - Lemon Tree Hotel\",\"53\":\"Bawarchi\",\"54\":\"Repete Brewery & Kitchen\",\"55\":\"Glocal Junction\",\"56\":\"Dock Forty Five\",\"57\":\"The Lal Street - Bar Exchange\",\"58\":\"Meridian Cafe & Restaurant\",\"59\":\"Tabula Rasa Cafe & Bar\",\"60\":\"Club Rogue\",\"61\":\"Heart Cup Coffee\",\"62\":\"Karma - Lounge \\u2022 Bar\",\"63\":\"10 Downing Street\",\"64\":\"Free Flow - Traffic Bar\",\"65\":\"Mad About China\",\"66\":\"Urban Asia - Kitchen & Bar\",\"67\":\"Air Live\",\"68\":\"FIREWATER  Kitchen & Bar\",\"69\":\"WOK Republic\",\"70\":\"Chutneys\",\"71\":\"Smoky Pitara\",\"72\":\"Revolt\",\"73\":\"WOK Republic\",\"74\":\"Amara - Trident Hyderabad\",\"75\":\"A'La Liberty\",\"76\":\"Kobe Sizzler\",\"77\":\"Bonsai\",\"78\":\"Saffron Soul - Marigold Hotel\",\"79\":\"Ohri's Ming's Court\"},\"Restaurant locality address\":{\"0\":\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1\":\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"2\":\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"3\":\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"4\":\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"5\":\"Green Lands, Begumpet, Hyderabad\",\"6\":\"2nd Floor, Sun Towers, Sector 1, Huda Techno Enclave, Above Mangatrai Jewellers, Madhapur, Hyderabad\",\"7\":\"1200, Road 59, Jubilee Hills, Hyderabad\",\"8\":\"790, Rangoli Building, Road 36, Jubilee Hills, Hyderabad\",\"9\":\"304, Puppalaguda, Financial District,ISB - Outer Ring Road, Gachibowli, Hyderabad\",\"10\":\"271-A, Road no. 10, Jubilee Hills, Hyderabad\",\"11\":\"882\\/A Road No 45, Jubilee Hills, Hyderabad\",\"12\":\"8-2-686\\/d, Above Good Earth, Road 12, Banjara Hills, Hyderabad\",\"13\":\"8-2-293\\/82\\/A\\/473, Road 36, Beside Nissan Showroom, Jubilee Hills, Hyderabad\",\"14\":\"Plot 1335\\/A, Road 45, Jubilee Hills, Hyderabad\",\"15\":\"The Westin, Mindspace IT Park, Hitech City, Hyderabad\",\"16\":\"Plot 624-B, Lane Beside Neerus Emporio, Road 35, Jubilee Hills, Hyderabad\",\"17\":\"1st Floor,SL Jubilee, Road 36, Jubilee Hills, Hyderabad\",\"18\":\"Holiday Inn Express & Suites, Gachibowli, Hyderabad\",\"19\":\"Kondapur, Hyderabad\",\"20\":\"Plot 753, Road 36, Jubilee Hills, Hyderabad\",\"21\":\"Shilpa Arcade, Road 3, Banjara Hills, Hyderabad\",\"22\":\"Ground and 1st Floor, Niharika Jubilee One, Road 1, Jubilee Hills, Hyderabad\",\"23\":\"Shop 8-2-686\\/8\\/6\\/A, 12th Square, Road 12, Banjara Hills, Hyderabad\",\"24\":\"Khanchand Towers, Opposite Hotel Taj Banjara, Road 1, Banjara Hills, Hyderabad\",\"25\":\"Lemon Tree Premier, Plot 2, Survey 64, Hitech City, Hyderabad\",\"26\":\"Ground Floor, Western Pearl Building, Survey 13, Kondapur, Hyderabad\",\"27\":\"2nd Floor, Aryans, Near Apollo Hospital, Road 92, Film Nagar, Hyderabad\",\"28\":\"3-5-908\\/1\\/2\\/3, Pooja Manor, Opposite TVS Showroom, Himayath Nagar, Hyderabad\",\"29\":\"The Purple Leaf Hotel, Karkhana, Secunderabad\",\"30\":\"Plot No 128\\/A, Road No 11, Jubilee Hills, Hyderabad\",\"31\":\"10th Floor, Sheraton Hyderabad Hotel, 115\\/1, ISB Road, Financial District, Nanakramguda, Gachibowli, Hyderabad\",\"32\":\"Plot B 2, Survey  6\\/1, Quiet Lands, Gachibowli, Hyderabad\",\"33\":\"Plot 1102, 5th Floor, Jaya Chambers, Road 36, Jubilee Hills, Hyderabad\",\"34\":\"Holiday Inn Express & Suites, Gachibowli, Hyderabad\",\"35\":\"Road 45, Jubilee Hills, Hyderabad\",\"36\":\"B 7 & 8, Jubilee Garden, Behind TCS Building, E Park, Kondapur, Hyderabad\",\"37\":\"5th Floor, Shreshta Aura, Road 36, Jubilee Hills, Hyderabad\",\"38\":\"373, Opposite UCO Bank, Jawahar Colony, Road 10, Jubilee Hills, Hyderabad\",\"39\":\"6-3-1239\\/4\\/1, Renuka Enclave, Raj Bhavan Road, Somajiguda, Hyderabad\",\"40\":\"1-120\\/3, Hitech City Road, HUDA Techno Enclave, Near Indian Bank, Madhapur, Hyderabad\",\"41\":\"Plot 66, Jyothi Celeste, Kavuri Hills, Madhapur, Hyderabad\",\"42\":\"Ground Floor, Sri Hari Building, Telgu Academy Road, Opposite Andhra Bank, Himayath Nagar, Hyderabad\",\"43\":\"Alcazar Mall, 498, Road 36, Venkatagiri Jubilee Hills, Hyderabad\",\"44\":\"NTR Gardens, Beside Prasads IMAX, Saifabad, Necklace Road, Hyderabad\",\"45\":\"Plot 6-3-247, Lakshmi Nivas, Beside Kusum Showroom, Road 1, Banjara Hills, Hyderabad\",\"46\":\"Opposite NIN Bus Stop, Vijayapuri Colony, Lalaguda road, Tarnaka, Hyderabad\",\"47\":\"Hyderabad Marriott Hotel & Convention Centre, Opposite Hussain Sagar Lake,Tank Bund Road, Near, Necklace Road, Hyderabad\",\"48\":\"A1, 1st Avenue, Sainikpuri, Secunderabad\",\"49\":\"8-2-686\\/K\\/2 E3, 4th Floor, Kimtee Square, NBT Nagar, Road 12, Banjara Hills, Hyderabad\",\"50\":\"ITC Kakatiya, 6-3-1187, Begumpet, Hyderabad\",\"51\":\"Tourism Plaza Paryatak Bhavan, Greenlands, Begumpet, Hyderabad\",\"52\":\"Lemon Tree Hotel, Survey 115\\/1, Financial District, Nanakramguda, Serilingampally, Gachibowli, Hyderabad\",\"53\":\"Beside Astoria Hotel, RTC Cross Road, Chikkadpally, Nallakunta, Hyderabad\",\"54\":\"Plot 644, Road 36, Jubilee Hills, Hyderabad\",\"55\":\"First Floor, Signature Towers, Opposite Botanical Garden, Kondapur Junction, Hyderabad\",\"56\":\"1066, Road 45, Jubilee Hills, Hyderabad\",\"57\":\"Level 2, SLN Terminus Mall, Gachibowli, Hyderabad\",\"58\":\"6-3-697\\/1, Panjagutta Cross Road, Panjagutta, Hyderabad\",\"59\":\"Beside Blue Cross, Road no 35, Jubilee hills, Hyderabad \",\"60\":\"Level 2, SLN Terminus Mall, Gachibowli, Hyderabad\",\"61\":\"Plot 1179, Road 45, Jubilee Hills, Hyderabad\",\"62\":\"8th Floor, Shangri La Towers, Road 2, Banjara Hills, Hyderabad\",\"63\":\"10, Ground Floor, My Home Tycoon, Begumpet, Hyderabad\",\"64\":\"4th Floor, Plot 566, Road 92, Jubilee Hills, Hyderabad\",\"65\":\"4th Floor, Food Court, Inorbit Mall, Hitech City, Hyderabad\",\"66\":\"1259\\/A, 3rd Floor, Beside Heritage Fresh, Road 36, Jubilee Hills, Hyderabad\",\"67\":\"5th Floor, Odyssey Mall, Road 36, Jubilee Hills, Hyderabad\",\"68\":\"5th Floor, Phoenix Tower A, Opposite Trident Hotel, Hitech City, Hyderabad\",\"69\":\"Shop 6, Lumbini Amrutha Chambers, Nagarjuna Circle, Banjara Hills, Hyderabad\",\"70\":\"Near More Super Market, Road 36, Jubilee Hills, Hyderabad\",\"71\":\"First Floor, Plot 1217\\/A, Road 36, Jubilee Hills, Hyderabad\",\"72\":\"2nd Floor, 644, Road 36, Jubilee Hills, Hyderabad neerus emporium.\",\"73\":\"2-43\\/A\\/6, Ground Floor, MM Heights, Pillar 28, Sri Ram Nagar Colony, Madhapur, Hyderabad\",\"74\":\"Trident Hyderabad, Opposite Cyber Towers, Hitech City, Hyderabad\",\"75\":\"3rd Floor, CyberGrub, Hitech City Main Road, Phase 2, Hitech City, Hyderabad\",\"76\":\"Opposite Film Nagar Club, Road 82, Film Nagar, Hyderabad\",\"77\":\"4th Floor, Plot 19, Besides Bajaj Electronics, Ravi Colony, Kondapur, Hyderabad\",\"78\":\"Green Lands, Begumpet, Hyderabad\",\"79\":\"5-9-30\\/16-20, Ohri's Cuisine Court, Opposite Old Gandhi Medical College, Basheer Bagh, Hyderabad\"},\"Average budget for two people\":{\"0\":1500,\"1\":2200,\"2\":1500,\"3\":2200,\"4\":1500,\"5\":2500,\"6\":1300,\"7\":1800,\"8\":1440,\"9\":1500,\"10\":1700,\"11\":2200,\"12\":1500,\"13\":1000,\"14\":1600,\"15\":2500,\"16\":1500,\"17\":1600,\"18\":1500,\"19\":250,\"20\":1800,\"21\":900,\"22\":1700,\"23\":1500,\"24\":450,\"25\":1700,\"26\":1500,\"27\":2600,\"28\":350,\"29\":1100,\"30\":1000,\"31\":1750,\"32\":1500,\"33\":1300,\"34\":1900,\"35\":1100,\"36\":1800,\"37\":800,\"38\":1100,\"39\":1100,\"40\":500,\"41\":1050,\"42\":550,\"43\":1600,\"44\":950,\"45\":1100,\"46\":550,\"47\":2900,\"48\":700,\"49\":800,\"50\":2000,\"51\":800,\"52\":1700,\"53\":750,\"54\":1500,\"55\":1200,\"56\":1400,\"57\":1300,\"58\":550,\"59\":1300,\"60\":1200,\"61\":1600,\"62\":1800,\"63\":1800,\"64\":1600,\"65\":600,\"66\":1300,\"67\":1500,\"68\":1300,\"69\":550,\"70\":900,\"71\":1000,\"72\":800,\"73\":550,\"74\":2600,\"75\":1300,\"76\":1100,\"77\":1000,\"78\":1500,\"79\":1000},\"Zomato user rating\":{\"0\":\"4.9\",\"1\":\"4.9\",\"2\":\"4.8\",\"3\":\"4.8\",\"4\":\"4.6\",\"5\":\"4.6\",\"6\":\"4.5\",\"7\":\"4.5\",\"8\":\"4.5\",\"9\":\"4.5\",\"10\":\"4.5\",\"11\":\"4.5\",\"12\":\"4.5\",\"13\":\"4.4\",\"14\":\"4.4\",\"15\":\"4.4\",\"16\":\"4.4\",\"17\":\"4.4\",\"18\":\"4.4\",\"19\":\"4.4\",\"20\":\"4.3\",\"21\":\"4.3\",\"22\":\"4.3\",\"23\":\"4.3\",\"24\":\"4.3\",\"25\":\"4.3\",\"26\":\"4.3\",\"27\":\"4.3\",\"28\":\"4.3\",\"29\":\"4.3\",\"30\":\"4.3\",\"31\":\"4.3\",\"32\":\"4.2\",\"33\":\"4.2\",\"34\":\"4.2\",\"35\":\"4.2\",\"36\":\"4.2\",\"37\":\"4.2\",\"38\":\"4.2\",\"39\":\"4.2\",\"40\":\"4.2\",\"41\":\"4.2\",\"42\":\"4.2\",\"43\":\"4.2\",\"44\":\"4.2\",\"45\":\"4.2\",\"46\":\"4.2\",\"47\":\"4.2\",\"48\":\"4.2\",\"49\":\"4.2\",\"50\":\"4.2\",\"51\":\"4.2\",\"52\":\"4.2\",\"53\":\"4.0\",\"54\":\"4.1\",\"55\":\"4.1\",\"56\":\"4.1\",\"57\":\"4.1\",\"58\":\"4.1\",\"59\":\"4.1\",\"60\":\"4.1\",\"61\":\"4.1\",\"62\":\"4.1\",\"63\":\"4.1\",\"64\":\"4.1\",\"65\":\"4.1\",\"66\":\"4.1\",\"67\":\"4.1\",\"68\":\"4.1\",\"69\":\"4.1\",\"70\":\"4.1\",\"71\":\"4.1\",\"72\":\"4.1\",\"73\":\"4.1\",\"74\":\"4.1\",\"75\":\"4.1\",\"76\":\"4.1\",\"77\":\"4.1\",\"78\":\"4.1\",\"79\":\"4.1\"}}"}
    - action_restaurant
    - slot{"query_restaurant_search": "Karachi Bakery in Khanchand Towers, Opposite Hotel Taj Banjara, Road 1, Banjara Hills, Hyderabad has been rated 4.3\nKing And Cardinal Bakery in 3-5-908/1/2/3, Pooja Manor, Opposite TVS Showroom, Himayath Nagar, Hyderabad has been rated 4.3\nHere's What's Cookin' in 1-120/3, Hitech City Road, HUDA Techno Enclave, Near Indian Bank, Madhapur, Hyderabad has been rated 4.2\nWOK Republic in Ground Floor, Sri Hari Building, Telgu Academy Road, Opposite Andhra Bank, Himayath Nagar, Hyderabad has been rated 4.2\nKim Fung in Opposite NIN Bus Stop, Vijayapuri Colony, Lalaguda road, Tarnaka, Hyderabad has been rated 4.2\n"}
    - utter_restaurant_search_results
    - utter_ask_send_email
* affirm
    - utter_ask_email
* send_email{"email": "sumalatha.b6@gmail.com"}
    - slot{"email": "sumalatha.b6@gmail.com"}
    - action_email
    - utter_goodbye
    - export
