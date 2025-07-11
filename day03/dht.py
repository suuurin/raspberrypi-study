# pip install adafruit-circuitpython-dht
# sudo apt install libgpiod2

import time
import adafruit_dht
import board

dht = adafruit_dht.DHT11(board.D23)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        print("Temp: ", temperature)
        print("Humi: ", humidity)
        time.sleep(1)

    except RuntimeError as error:
        print(error.args[0])

    except KeyboardInterrupt:
        print("사용자 종료")
        break
