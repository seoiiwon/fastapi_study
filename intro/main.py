from fastapi import FastAPI, Query
from typing import List, Dict

app = FastAPI() # FastAPI 인스턴스 생성

@app.get("/") # 데코레이터를 사용해서 "/" 경로에 대한 HTTP GET 요청을 어떤 함수가 처리할지 지정
def read_root(): # GET 요청을 처리할 함수
    return {"message": "Hello, World!"} # JSON 형태의 응답 반환 (FastAPI가 자동으로 JSON 형식으로 반환)

@app.get("/items/{item_id}")
def read_item(item_id : int):
    return {"item_id" : item_id}

@app.get("/getdata/")
def read_items(data: str = "funcoding"):
    return {"data" : data}

@app.get("users/{user_id}/items/{item_name}")
def read_user_item(user_id, item_name):
    return {"user_id" : user_id, "item_name" : item_name}

@app.get("/items/")
def read_items(skip = 0, limit = 10):
    return {"skip" : skip, "limit" : limit}

@app.get("/students/")
def read_students(students: List[int] = Query([])):
    return {"students" : students}

@app.post("/create-student/")
def create_student(student: Dict[str, int]):
    return student
