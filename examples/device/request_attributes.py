

import logging
import time

from tb_device_mqtt import TBDeviceMqttClient
logging.basicConfig(level=logging.INFO)


def on_attributes_change(result, exception=None):
    # This is a callback function that will be called when we receive the response from the server
    if exception is not None:
        logging.error("Exception: " + str(exception))
    else:
        logging.info(result)


def main():
    client = TBDeviceMqttClient("127.0.0.1", username="A2_TEST_TOKEN")
    client.connect()
    # Sending data to retrieve it later
    client.send_attributes({"atr1": "value1", "atr2": "value2"})
    # Requesting attributes
    client.request_attributes(["atr1", "atr2"], callback=on_attributes_change)
    try:
        # Waiting for the callback
        while not client.stopped:
            time.sleep(1)
    except KeyboardInterrupt:
        client.disconnect()
        client.stop()


if __name__ == '__main__':
    main()
