from pydantic import BaseModel, Field,validator
from typing import Dict

class ServerRegisterModel(BaseModel):
    server_name: str
    callback_url: str
    Os_username: str
    Os_password: str


@validator('server_name', 'callback_url', 'Os_username','Os_password')
def field_required(cls, value):
    if not value:
        raise ValueError('field required')
    return value

