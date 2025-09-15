

import logging

from tb_device_mqtt import TBDeviceMqttClient
logging.basicConfig(level=logging.DEBUG)

IOTPLATFORM_HOST = "127.0.0.1"
DEVICE_ACCESS_TOKEN = "DEVICE_ACCESS_TOKEN"

SECRET_KEY = "DEVICE_SECRET_KEY"  # Customer should write this key in device claiming widget
DURATION = 30000  # In milliseconds (30 seconds)


def main():
    client = TBDeviceMqttClient(IOTPLATFORM_HOST, username=DEVICE_ACCESS_TOKEN)
    client.connect()
    info = client.claim(secret_key=SECRET_KEY, duration=DURATION)
    if info.rc() == 0:
        print("Claiming request was sent.")
    client.stop()


if __name__ == '__main__':
    main()
