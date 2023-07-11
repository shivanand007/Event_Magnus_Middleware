from pydantic import BaseModel,validator


class Register(BaseModel):
    App_name : str
    Origin_server_Ip : str
    Os_username : str
    Os_password : str


@validator('App_name', 'Origin_server_Ip', 'Os_username', 'Os_password')
def field_required(cls, value):
    if not value:
        raise ValueError('field required')
    return value
