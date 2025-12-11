from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import requests

joke_lst = []

def fetch_jokes():
    joke_url = "https://official-joke-api.appspot.com/jokes/random/25"
    try:
        jokes_lst = requests.get(joke_url)
        return jokes_lst.json()
    except requests.exceptions.HTTPError as err:
        return []
    except requests.exceptions.RequestException as e: 
        return []

def get_joke():
    global joke_lst
    if not joke_lst:
        joke_lst = fetch_jokes()
    if joke_lst:
        joke_data = joke_lst.pop()
        return joke_data['setup'] + "\n" + joke_data['punchline']
    return "Sorry girl! I don't got no more jokes"
    
    
    
class ActionTellJoke(Action):

    def name(self) -> Text:
        return "action_tell_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        joke_text = get_joke()
        dispatcher.utter_message(text=joke_text)
        
        return []

       