from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    rollno: int
    name: str
    grade: str

app = FastAPI()
@app.get("/")
def home():
    return {"page": "Home"}
@app.get("/about")
def about():
    return {"page": "About","Author":"Cherry"}
@app.get("/health")
def health():
    return {"status": "healthy"}
@app.post("/create")
def create_item():
    return {"item": "created"}
@app.get("/student/{rollno}")
def get_student(rollno):
    return {"Result":"Distinction", "rollno": rollno}
@app.get("/Candidate/{rollno}")
def get_Candidate(rollno: int): 
    return {"Result":"Distinction","rollno": rollno, "Type":str(type(rollno))}
@app.post("/items")
def create_item(item: Student):
    return {"rollno": item.rollno, "name": item.name, "grade": item.grade}
