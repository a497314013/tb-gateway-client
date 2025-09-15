

import logging

from tb_gateway_mqtt import TBGatewayMqttClient
logging.basicConfig(level=logging.DEBUG)

IOTPLATFORM_HOST = "127.0.0.1"
GATEWAY_ACCESS_TOKEN = "GATEWAY_ACCESS_TOKEN"

DEVICE_NAME = "DEVICE_NAME"
SECRET_KEY = "DEVICE_SECRET_KEY"  # Customer should write this key in device claiming widget
DURATION = 30000  # In milliseconds (30 seconds)


def main():
    client = TBGatewayMqttClient(IOTPLATFORM_HOST, username=GATEWAY_ACCESS_TOKEN)
    client.connect()

    """
    You are able to provide every parameter or pass claiming request like:
    request_example = {
                       "DEVICE A": {
                           "secretKey": "DEVICE_A_SECRET_KEY",
                           "durationMs": "30000"
                           },
                       "DEVICE B": {
                           "secretKey": "DEVICE_B_SECRET_KEY",
                           "durationMs": "60000"
                       }
    
    info = client.gw_claim(claiming_request=request_example).wait_for_publish()
    
    """

    client.gw_connect_device(DEVICE_NAME)

    info = client.gw_claim(device_name=DEVICE_NAME, secret_key=SECRET_KEY, duration=DURATION)

    if info.rc() == 0:
        print("Claiming request was sent.")
    client.stop()


if __name__ == '__main__':
    main()
