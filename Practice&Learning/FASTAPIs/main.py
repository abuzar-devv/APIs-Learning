#In this file i practiced  basic path operations using postman


from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

@app.get("/")
def test():
    return {"Test":"Successful"}

@app.get("/status")
def test_2():
    return {
    "status": "running",
    "version": "1.0"
}

@app.get("/about")
def test_3():
    return {"Test 3":"Successful"}

@app.post("/post")
def test_4():
    return {"Test 4":"successful"}

@app.post("/students")
def posting(payload : dict=Body()):
    return {
        "Request":"Recieved",
        "Name":payload["name"],
        "Age":payload["age"],
        "program":payload["program"]
    }
