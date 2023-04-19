def userSr(user) -> dict:
    return {
        "id" : str(user["_id"]),
        "email" : user["email"],
        "bio" : user["bio"],
        "fullName" : user["fullName"]
    }

def commentSr(comment) -> dict:
    return {
        "id" : str(comment["_id"]),
        "user" : comment["user"],
        "comment" : comment["comment"]
    }

def commentsSr(comments) -> list:
    return [commentSr(comment) for comment in comments]

def usersSr(users) -> list:
    return [userSr(user) for user in users]