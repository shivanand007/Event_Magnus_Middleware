import os
from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi import FastAPI,Body
from typing import Any
import datetime

''' Internal Imports'''
from app.utils import ServerRegisterModel
from app.utils import logger
from app.utils import write_data,read_data


server_router = APIRouter()

@server_router.post('/server_subscribe',tags=["Subscribe Webhook"], summary="Register Your Server and Subscribe for events")
def server_register(server_data:ServerRegisterModel) -> Any:
    try:
        logger.info(f"New Registeration by Server with Name : {server_data.server_name} || callback_url : {server_data.callback_url} || Os_username: {server_data.Os_username}")

        #defing dict
        server_id_hashset = {}

        # storing this to hashmap
        server_id_hashset[server_data.server_name] = server_data.callback_url

        # writing in file
        write_data(server_id_hashset, os.environ.get('server_hashset_file_path'))

        # reading form file
        data = read_data(os.environ.get('server_hashset_file_path'))

        logger.debug(f" {server_data.server_name} : {server_data.callback_url} ")
        logger.debug(f"Hashmap File contains : {data}")

        return "server subscribed with call back url : " + server_data.callback_url + " from " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        logger.critical(f"There was error in server Registration : {e}", stack_info=True)
        return {"Failed to Subcribe for Webhook events, Contact Application Owner"}

