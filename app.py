from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

data = []

class Person(BaseModel):
    name: str
    occupation: str
    address: str



@app.get("/person")
def get_all_persons():
    return data

@app.post("/person")
async def add_person(request_person: Person):
    new_add = jsonable_encoder(request_person)
    
    
 
    if (not new_add["name"] == "") and (not new_add["occupation"] == "")and (not new_add["address"] == ""):
        data.append(new_add)
        return {
            "success": True,
            "result": new_add
    }
    else:
        return{
            "success": False,
            "result": {
                "error_message": "invalid request"
        }
        }

      