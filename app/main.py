from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import os

app = FastAPI(title="Data Pipeline")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def home(request: Request):
    return {"message": "Welcome to the Data Pipeline API"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
