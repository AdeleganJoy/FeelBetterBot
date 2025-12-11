import requests
import aiohttp
import asyncio

joke_lst = []


async def fetch_jokes():
    joke_url = "https://official-joke-api.appspot.com/jokes/random/25"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(joke_url) as res:
                jokes_lst = await res
                return jokes_lst
            
    except requests.exceptions.HTTPError as err:
        return []
    except requests.exceptions.RequestException as e: 
        return []
    
asyncio.run(fetch_jokes())
#https://blog.jonlu.ca/posts/async-python-http