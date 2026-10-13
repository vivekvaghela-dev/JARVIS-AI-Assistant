import os
import sys

import requests
import logging
from dotenv import load_dotenv
from livekit.agents import function_tool
from datetime import datetime
import webbrowser #online serach mate
import urllib.parse #@online serach mate
# Load environment variable
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@function_tool
async def google_search(query: str) -> str:
    logger.info(f"Query प्राप्त हुई।: {query}")

    api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")

    if not api_key or not search_engine_id:
        logger.error("API key या Search Engine ID missing है।")
        return "Environment variables में API key या Search Engine ID missing है।"

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query,
        "num": 3
    }

    logger.info("Google Custom Search API को request भेजी जा रही है...")
    response = requests.get(url, params=params)

    if response.status_code != 200:
        logger.error(f"Google API में error आया: {response.status_code} - {response.text}")
        return f"Google Search API में error आया: {response.status_code} - {response.text}"

    data = response.json()
    results = data.get("items", [])

    if not results:
        logger.info("कोई results नहीं मिले।")
        return "कोई results नहीं मिले।"

    formatted = ""
    logger.info("Search results:")
    for i, item in enumerate(results, start=1):
        title = item.get("title", "No title")
        link = item.get("link", "No link")
        snippet = item.get("snippet", "")
        formatted += f"{i}. {title}\n{link}\n{snippet}\n\n"
        logger.info(f"{i}. {title}\n{link}\n{snippet}\n")

    return formatted.strip()

@function_tool
async def get_current_datetime() -> str:
    return datetime().now.isoformate()



#online youtube,google search etc search krva mate jarvis khud krse user ni requiremtnts mujab
import webbrowser
import urllib.parse

@function_tool
async def youtube_search(query: str) -> str:
    """YouTube par diye gaye query ko search karke browser mein kholta hai"""
    try:
        encoded_query = urllib.parse.quote(query)
        url = f"https://www.youtube.com/results?search_query={encoded_query}"
        webbrowser.open(url)
        logger.info(f"YouTube search kiya gaya: {query}")
        return f"YouTube par '{query}' search kar diya hai, browser mein khul gaya hai."
    except Exception as e:
        logger.error(f"YouTube search mein error: {e}")
        return "YouTube search karte samay error aaya."

@function_tool
async def google_open_search(query: str) -> str:
    """Google par diye gaye query ko search karke browser mein kholta hai"""
    try:
        encoded_query = urllib.parse.quote(query)
        url = f"https://www.google.com/search?q={encoded_query}"
        webbrowser.open(url)
        logger.info(f"Google search kiya gaya: {query}")
        return f"Google par '{query}' search kar diya hai, browser mein khul gaya hai."
    except Exception as e:
        logger.error(f"Google search mein error: {e}")
        return "Google search karte samay error aaya."