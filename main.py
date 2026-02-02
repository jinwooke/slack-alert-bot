import requests
import random
import time
from datetime import datetime, timedelta

WEBHOOK = "여기에_웹훅_붙여넣기"

MESSAGES = [
    "물 마셔!",
    "스트레칭!",
    "집중 타임!",
    "잠깐 쉬기!"
]


def send(msg):
    requests.post(WEBHOOK, json={"text": msg})


def random_delay():
    # 1~3시간 랜덤 (테스트용)
    return random.randint(1, 3)


while True:
    send(random.choice(MESSAGES))
    time.sleep(random_delay())
