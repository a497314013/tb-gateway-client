

import logging
import time

from tb_gateway_mqtt import TBGatewayMqttClient
logging.basicConfig(level=logging.INFO)


def callback(result, exception=None):
    if exception is not None:
        logging.error("Exception: " + str(exception))
    else:
        logging.info(result)


def main():
    gateway = TBGatewayMqttClient("127.0.0.1", username="TEST_GATEWAY_TOKEN")
    gateway.connect()
    # Requesting attributes
    gateway.gw_request_shared_attributes("Example Name", ["temperature"], callback)

    try:
        # Waiting for the callback
        while not gateway.stopped:
            time.sleep(1)
    except KeyboardInterrupt:
        gateway.disconnect()
        gateway.stop()


if __name__ == '__main__':
    main()
