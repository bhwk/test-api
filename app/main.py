from fastapi import FastAPI, status

app = FastAPI()


@app.get("/health")
def health():
    return status.HTTP_200_OK


@app.get("/test", status_code=status.HTTP_200_OK)
def test_route():
    return {"message": "route is active"}
