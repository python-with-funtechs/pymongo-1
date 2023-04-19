from pydantic import *

class Comment(BaseModel):
    user : str
    comment : str
