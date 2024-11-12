from typing import TypeVar, Generic
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

# 타입 변수 T를 선언한다. -> 커스텀 제네릭 타입을 만들기 위한 첫 단계
T = TypeVar('T')

# Generic[T]를 상속받는 클래스를 정의함으로써, GenericItem은 어떤 타입 T도 받을 수 있는 제네릭 클래스가 된다.
class GenericItem(BaseModel, Generic[T]):
    name: str
    content: T # content 타입은 동적으로 결정

@app.post("/generic_items/")
def create_item(item: GenericItem[int]):
    return {"item" : item.dict()}