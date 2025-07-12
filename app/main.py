from fastapi import FastAPI, status

app = FastAPI()


@app.get("/health")
def health():
    return status.HTTP_200_OK
