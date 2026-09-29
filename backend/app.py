from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from calculator import calculator_expression
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
    expression : str

@app.post("/calculate")
def calculate(data : Input):
    result = calculator_expression(data.expression)
    if result == "Invalid Expression":
        raise HTTPException(
            status_code = 400,
            detail = "Invalid Expression"
    )
    if result == "cannot divide by zero":
        raise HTTPException(
            status_code = 400,
            detail = "cannot divide by zero"
        )
    return {"Result" : result}
    
