export env=local
export api_key={your_upstage_api_key}

uvicorn app.main:app --host localhost --port 8080 --reload
