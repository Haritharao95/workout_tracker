import requests
from datetime import datetime
import os


APP_ID= os.environ["APP_ID"]
APP_KEY= os.environ["APP_KEY"]

exercise_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint=os.environ["sheet_endpoint"]

exercise_text=input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key":APP_KEY,
}

parameters={
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 165,
    "age": 28,
}



response=requests.post(exercise_endpoint,json=parameters,headers=headers)
result=response.json()
print(result)

today_date=datetime.now().strftime("%d/%m/%Y")
now_time=datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs={
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

bearer_headers={
    "Authorization": os.environ["Authorization"]
}

sheet_response=requests.post(sheet_endpoint,json=sheet_inputs,headers=bearer_headers)
print(sheet_response.text)
