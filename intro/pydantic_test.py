from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Union

app = FastAPI()

class Bedorage(BaseModel):
    name: str
    tags: List[str]
    variant: Union[int, str]

@app.post("/bedorage/")
def create_bedorage(Bedorage: Bedorage):
    return {"bedorage" : Bedorage.dict()}

class Image(BaseModel):
    url: str
    name: str

class ChimChackMan(BaseModel):
    name: str
    description: str
    image: Image

@app.post("/chim/")
def create_Chim(Chim: ChimChackMan):
    return {"Chim" : Chim.dict()}

class Item(BaseModel):
    # name은 필수 필드이며, 최소 2자, 최대 50자
    name: str = Field(..., title="Item Name", min_length=2, max_length=50)
    # description은 선택 필드이며, 최대 300자
    description: str = Field(None, description="The description of the item", max_length=300)
    # price는 필수 필드이며, 0보다 커야함
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    # tag는 선택 필드이며, 기본값으로 빈 리스트를 가짐
    tag: List[str] = Field(default=[], alias="item-tags")

@app.post("/items/")
async def create_item(item: Item):
    return {"item" : item.dict()}