from config.config import users , comments
from fastapi import APIRouter
from schemas.Schema import usersSr , commentsSr , userSr ,commentSr
from models.comment import Comment
from models.user import User
from bson import ObjectId


all_routes = APIRouter()

@all_routes.get("/")
def getHome():
    return {"status": 200 , "message":"Welcome to the users api"}

@all_routes.post("/add/user")
async def getAllUsers(user:User):
   insertedDoc = users.insert_one(dict(user))
   return userSr(users.find_one({"_id" : insertedDoc.inserted_id}))

#get all users
@all_routes.get("/all/users")
async def getAllUsers():
    getDocs = usersSr(users.find())
    return getDocs

#get one user
@all_routes.get("/user/{id}")
async def getUser(id:str):
    getOne = userSr(users.find_one({"_id" : ObjectId(id)}))
    return getOne

#update a user
@all_routes.patch("/update/{id}")
async def updateDoc(id:str , user:User):
  users.find_one_and_update(
        {"_id" : ObjectId(id)} , {"$set" : dict(user)}
    )
  return "Updated succesfully"

#delete user
@all_routes.delete("/delete/{id}")
async def deleteUser(id:str):
   users.find_one_and_delete({"_id" : ObjectId(id)})
   return {"status" : "Ok" , "message" : "Deleted successfully"}