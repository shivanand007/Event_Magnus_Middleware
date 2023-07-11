"""
This module will help user register and get the unique hashed App_Id

This App_Id will be stored in .env file, but in furture can be replaced to database
"""
from fastapi import APIRouter
from fastapi import FastAPI,Body
import os
from dotenv import load_dotenv

''' Internal Imports '''
from app.utils import Register
from app.utils import logger
from app.utils import write_data,read_data

import hashlib

register_router = APIRouter()

@register_router.post("/Token", tags=["Authentication"], summary="Get Your Unique App Id")
def get_app_id(hash:Register) -> str:
    try:
        logger.info(f"New Registeration Request by Client with App Name : {hash.App_name} || Ip : {hash.Origin_server_Ip} || Os_username: {hash.Os_username}")
        # Concatenate the username and IP address
        input_str = f"{hash.Os_username}{hash.Origin_server_Ip}"

        # Hash the input string using SHA-256
        hashed_str = hashlib.sha256(input_str.encode()).hexdigest()

        app_id = hashed_str

        #defing dict
        App_Id_Hashset = {}

        # loading eviroment variables for accessing os variables
        load_dotenv()

        # storing this to hashmap
        App_Id_Hashset[hash.App_name] = app_id

        # writing in file, by passing file path
        write_data(App_Id_Hashset,os.environ.get('client_hashset_file_path'))

        # reading form file
        data = read_data(os.environ.get('client_hashset_file_path'))

        logger.debug(f"App Id value for client {hash.App_name} : {app_id}")
        logger.debug(f"Hashmap File contains : {data}")

        #app_id_res = [{"app_id":app_id}]
        return app_id
    except Exception as e:
        logger.critical(f"There was error in app_id Creation : {e}", stack_info=True)
    except ValueError:
        raise ValueError("Empty string is not allowed")