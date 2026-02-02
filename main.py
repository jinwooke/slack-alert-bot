import requests
import random
import schedule
import time
from datetime import datetime, timedelta
import os

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK")

MESSAGES = [
    "💧 물 마셔!",
    "🧘 스트레칭!",
    "🔥 집중 타임",
    "📚 공부 시작",
    "😴 잠깐 쉬기"
]


# ========= Slack 전송 =========
def send_slack(msg):
    requests.post(
        WEBHOOK_URL,
        json={"text": msg}
    )


# ========= 랜덤 시간 =========
def random_time(start=9, end=21):
    start_dt = datetime.now().replace(hour=start, minute=0)
    end_dt = datetime.now().replace(hour=end, minute=0)
    delta = end_dt - start_dt
    sec = random.randint(0, int(delta.total_seconds()))
    return (start_dt + timedelta(seconds=sec)).strftime("%H:%M")


def schedule_today():
    schedule.clear()

    for _ in range(2):
        t = random_time()
        schedule.every().day.at(t).do(send_slack, random.choice(MESSAGES))
        print("예약:", t)


schedule_today()

while True:
    schedule.run_pending()
    time.sleep(10)
