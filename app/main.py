from fastapi import FastAPI, Response, status
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter

app = FastAPI()

counter = Counter("app_requests_total", "Total requests to the app")


@app.middleware("http")
async def count_requests(request, call_next):
    counter.inc()
    response = await call_next(request)
    return response


@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    return {"status": "ok"}


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "hello world"}


@app.get("/test", status_code=status.HTTP_200_OK)
def test_route():
    return {"message": "route is active"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
