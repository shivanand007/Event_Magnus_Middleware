from fastapi import APIRouter
from fastapi import FastAPI,Body
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import os

''' Internal Imports '''
from app.utils import Task
from app.utils import logger,read_data,is_ip_reachable
from app.Callback import callback_algo


event_router = APIRouter()

@event_router.get("/", tags=["Home"])
async def home():
    # get_documentation()
    return RedirectResponse(url="/docs", status_code=200)

@event_router.post("/event",tags=["Communication"],summary="Post Events From Your Applications", description="This endpoint receives events from a third-party API, \n Note :- Prior Invoking these endpoint Get your App id from the Register Endpoint")
async def events(Item:Task = Body(...,embed=True)):
    try:
        logger.info(f"Event Recevied from third party Api with App_Name :{Item.app_name} || App_Id: {Item.app_id}")

        load_dotenv('.env')
        data = read_data(os.getenv('client_hashset_file_path'))

        ''' Primary Checking for Id App_id If It is registered with Middleware '''

        if data.get(Item.app_name,-1) == Item.app_id:
            logger.info(f"Client app Id verified,{Item.app_id} ")

            ''' Checking Ip is reachable and Confirming if Ip provided is in same network '''

            if is_ip_reachable(Item.destination_server_Ip,Item.port):
                logger.info(f"Destination server ip : {Item.destination_server_Ip} ")

                ''' Executing callback algorithhm function, to pass event msg client'''

                if callback_algo(Item.destination_server_url,Item.event_msg,Item.app_name):
                   return {f"Event is Securely Delivered to {Item.destination_server_url}"}, 200
                else:
                    return {"There was issue, while send your request to the desired server"}
            else:
                return {"Destination Ip address is not valid, Not Present in the Network"},401
        else:
            logger.error(f"user is not verified")
            return {"Invalid User ! Contact Application Owner AYFT, Refer Documentation Provided by AYFT"},401

    except Exception as e:
        logger.debug(f"error occured : {e}")
        return {"There was error processing your request"}


#event_app.include_router(event_router)

