from fastapi import FastAPI, Header, Response
from pydantic import BaseModel

app = FastAPI()
port = 8080

class FibonacciRequest(BaseModel):
    index: int

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/health')
def health_check():
    headers = {"System-Health": "true"}
    return Response(status_code=204, headers=headers)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@app.post('/fibonacci')
def calculate_fibonacci(request: FibonacciRequest):
    fib_index = request.index
    result = fibonacci(fib_index)
    return {"index": fib_index, "result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
