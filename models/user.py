from pydantic import *

class User(BaseModel):
    fullName : str
    email : str
    bio : str 