export env=local
export openai_api_key={your_openai_api_key}

uvicorn app.main:app --reload
