# FastAPI testing api

A simple FastAPI app with:
- CI/CD using github actions
- Docker containerization
- Pytest-based unit testing

## Run locally 

```bash
docker build -t testapi .
docker run -p 8000:8000 testapi
```

Then visit [here](http://localhost:8000/health).

## Run tests locally

```bash
pip install -r requirements.txt
pytest
```
