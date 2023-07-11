'''

This algorithm will take destination server url and callback the requested server

'''
import requests

import logging
import urllib.parse
from app.utils import logger



def callback_algo(destination_url, event_msg, app_name):


        logger.info("<----------- callback funcation Executed ----------> ")
        event_data = {
            "event" : event_msg,
            #"sent_by " : app_name
        }

        timeout_seconds = 10  # Set the timeout to 10 seconds

        logger.info(f" Destination URL Requested By User : {destination_url} with timeout {timeout_seconds} sec")
        # creating query string
        query_string = urllib.parse.urlencode(event_data)

        logger.info(f" Query String Objects : {query_string}")

        url = destination_url + query_string

        logger.info(f" Final url for destination server : - {url}")

        try:
            response = requests.get(url,timeout=timeout_seconds)

            if response.status_code == 200:
                logger.info("___________Callback Request successful! ________ ")
                logger.info(f"Callback Response content: {response.content}")
                return True
            else:
                logger.info(f"Callback Response content: {response.content} ")
                logger.info(f"Request failed with status code {response.status_code}")
                return False
        except requests.Timeout:
            logger.info("Request Timeout")
            return False

        except requests.RequestException as e:
            logger.info(f"Error Occured while Reaching :- {e}")
            return False


