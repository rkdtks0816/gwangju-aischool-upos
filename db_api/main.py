#! /usr/bin/python3

# 참고 -> https://soyoung-new-challenge.tistory.com/81
# http://bigdata.dongguk.ac.kr/lectures/DB/_book/python%EC%97%90%EC%84%9C-mysql%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98-%EC%A0%91%EA%B7%BC.html
# CORS : https://lucky516.tistory.com/108

# uvicorn main:app --reload --host=0.0.0.0 --port=8000
# uvicorn FemsMain:app --reload --host=0.0.0.0 --port=8888


import uvicorn                                      # Web Server
from fastapi import FastAPI, Response               # Json Response
from fastapi.responses import HTMLResponse          # HTML Response
from fastapi.middleware.cors import CORSMiddleware  # CORS
import Logger

# import json     # json
# import pymysql  # mariadb

# _logger = Logger.Logger("UposService")
import UposService  # implementation


app = FastAPI()

# CORS
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WAS


@app.get("/")
async def welcome():
    html_content = """
    <html>
    <br/>
    <br/>
    <head>
    <title>Welcome to UPOS Service!</title>
    <style>
    html { color-scheme: light dark; }
    body { width: 35em; margin: 0 auto;
    font-family: Tahoma, Verdana, Arial, sans-serif; }
    </style>
    </head>
    <body>
    <h1>Welcome to UPOS Service!</h1>
    <br/>
    <p>If you see this page, the uposREST web server is successfully working.</p>

    <p>For documentation and support please refer to swagger documents '.../docs'
    </a>.<br/>

    <p><em>Thank you for using UPOS Service.</em></p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# 전력량 - 일별 데이터
@app.get("/GetLpDataDaily")
async def GetLpDataDaily(startDate: str, endDate: str):
    result = await UposService.GetLpDataDaily(startDate, endDate)
    return Response(content=result, media_type="application/json")

# 전력량 - 시간별 데이터
@app.get("/GetLpDataHourly")
async def GetLpDataHourly(runDate: str):
    result = await UposService.GetLpDataHourly(runDate)
    return Response(content=result, media_type="application/json")

# AHU Data 조회
@app.get("/GetUpiData")
async def GetUpiData(runDate: str):
    result = await UposService.GetUpiData(runDate)
    return Response(content=result, media_type="application/json")

# Dashboard 
@app.get("/Get_ChilledWater_T_Data")
async def Get_ChilledWater_T_Data(runDate: str):
    result = await UposService.Get_ChilledWater_T_Data(runDate)
    return Response(content=result, media_type="application/json")

@app.get("/GetInfoData")
async def GetInfoData(szUnitID: str, runDate: str):
    result = await UposService.GetInfoData(szUnitID, runDate)
    return Response(content=result, media_type="application/json")

# GetnowefficiencyData 
@app.get("/GetnowefficiencyData")
async def GetnowefficiencyData(runDate: str):
    result = await UposService.GetnowefficiencyData(runDate)
    return Response(content=result, media_type="application/json")

# GetefficiencyData 
@app.get("/GetefficiencyData")
async def GetefficiencyData(runDate: str):
    result = await UposService.GetefficiencyData(runDate)
    return Response(content=result, media_type="application/json")

# Getrun_numData 
@app.get("/GetRunNumData")
async def GetRunNumData(runDate: str):
    result = await UposService.GetRunNumData(runDate)
    return Response(content=result, media_type="application/json")

# Getrun_numData 
@app.get("/GetMLData")
async def GetMLData(runDate: str):
    result = await UposService.GetMLData(runDate)
    return Response(content=result, media_type="application/json")