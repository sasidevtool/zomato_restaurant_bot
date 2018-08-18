## Generated Story 2182074300828345856
* greet
    - utter_greet
* restaurant_search{"location": "jabalpur"}
    - slot{"location": "jabalpur"}
    - validate_location
    - slot{"location": "jabalpur"}
    - get_all_search_results
    - slot{"location": "jabalpur"}
    - slot{"requested_slot": "cuisine"}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - validate_cuisine
    - slot{"cuisine": "mexican"}
    - get_all_search_results
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "price"}
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - validate_price
    - slot{"price": "2"}
    - get_all_search_results
    - slot{"price": "2"}
    - slot{"full_restaurant_search": "{\"Restaurant Name\":{\"0\":\"Coffee Culture\",\"1\":\"Coffee Culture\",\"2\":\"Coffee Culture\"},\"Restaurant locality address\":{\"0\":\"Main Road, Sadar Bazaar, Cantt, Jabalpur\",\"1\":\"Main Road, Sadar Bazaar, Cantt, Jabalpur\",\"2\":\"Main Road, Sadar Bazaar, Cantt, Jabalpur\"},\"Average budget for two people\":{\"0\":1200,\"1\":0,\"2\":1000},\"Zomato user rating\":{\"0\":\"0\",\"1\":\"0\",\"2\":\"0\"}}"}
    - action_restaurant
    - slot{"query_restaurant_search": null}
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_restaurant
    - slot{"query_restaurant_search": "Coffee Culture in Main Road, Sadar Bazaar, Cantt, Jabalpur has been rated 0\nCoffee Culture in Main Road, Sadar Bazaar, Cantt, Jabalpur has been rated 0\n"}
    - utter_restaurant_search_results
    - utter_ask_send_email
* deny
    - action_bye
    - reset_slots
    - export

