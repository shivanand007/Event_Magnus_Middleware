from pydantic import BaseModel,validator


class Task(BaseModel):
    app_name:str
    app_id : str
    event_msg : str
    destination_server_Ip: str
    destination_server_url : str
    Origin_server_Ip : str
    port : int

@validator('app_name','app_id', 'event_msg', 'destination_server_Ip', 'destination_server_endpoint', 'destination_server_url')
def field_required(cls, value):
    if not value:
        raise ValueError('field required')
    return value
