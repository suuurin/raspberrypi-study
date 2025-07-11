import mysql.connector
import adafruit_dht
import board
import time
from datetime import datetime

# --- DHT 센서 설정---
dht_pin = board.D23
dht_device = adafruit_dht.DHT11(dht_pin)

# --- MariaDB 설정 ---
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345',
    'database': 'testdht'
}

def store_dht_data(temperature, humidity):
    conn = None
    cursor = None
    try:
        # DB 연결
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # SQL 쿼리: 온도, 습도, 현재 시간을 dht_data 테이블에 삽입
        sql = "INSERT INTO dht_data (temperature, humidity, timestamp) VALUES (%s, %s, %s)"
        current_time = datetime.now() # 현재 시간 가져오기
        cursor.execute(sql, (temperature, humidity, current_time))
        conn.commit() # 변경사항 저장
        print(f"[{current_time}] 데이터 저장 성공: 온도={temperature:.2f}C, 습도={humidity:.2f}%")

    except mysql.connector.Error as err: # PyMySQL을 사용한다면 pymysql.Error as err:
        print(f"[{datetime.now()}] 데이터베이스 오류: {err}")
        if conn:
            conn.rollback() # 오류 발생 시 롤백
    except Exception as e:
        print(f"[{datetime.now()}] 예상치 못한 오류 발생: {e}")
    finally:
        # 사용한 리소스 정리
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

print("DHT 센서 데이터 수집 및 DB 저장 시작...")
while True:
    try:
        # DHT 센서에서 온도 및 습도 읽기
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        if temperature_c is not None and humidity is not None:
            store_dht_data(temperature_c, humidity) # 데이터베이스에 저장
        else:
            print(f"[{datetime.now()}] 센서에서 유효한 데이터를 읽지 못했습니다. 재시도합니다.")

    except RuntimeError as error:
        # DHT 센서 읽기 오류 (자주 발생할 수 있음)
        print(f"[{datetime.now()}] DHT 읽기 오류 (RuntimeError): {error.args[0]}")
    except Exception as e:
        # 기타 예상치 못한 오류 처리
        print(f"[{datetime.now()}] 예상치 못한 오류 발생: {e}")

    time.sleep(5) # 5초마다 데이터 읽기 시도import mysql.connector # 또는 import pymysql (위에서 설치한 라이브러리에 따라 선택)
