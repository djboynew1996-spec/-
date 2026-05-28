import time
from datetime import datetime
import pytz
import os

# กำหนดรายชื่อ timezone ที่ต้องการแสดง
TIMEZONES = [
    ('Bangkok', 'Asia/Bangkok'),
    ('UTC', 'UTC'),
    ('New York', 'America/New_York'),
    ('London', 'Europe/London'),
    ('Tokyo', 'Asia/Tokyo'),
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_clocks():
    while True:
        clear()
        now_utc = datetime.now(pytz.utc)
        print("=== Digital Clock (Multi Timezone) ===")
        for name, tz in TIMEZONES:
            cur_time = now_utc.astimezone(pytz.timezone(tz))
            print(f"{name:10}: {cur_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("\nPress Ctrl+C to exit.")
        time.sleep(1)

if __name__ == "__main__":
    try:
        show_clocks()
    except KeyboardInterrupt:
        print("\nExiting Digital Clock.")
