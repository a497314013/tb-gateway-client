

import logging
import time

from tb_device_mqtt import TBDeviceMqttClient
logging.basicConfig(level=logging.DEBUG)


def callback(result, *args):
    logging.info("Received data: %r", result)


def main():
    client = TBDeviceMqttClient("127.0.0.1", username="A2_TEST_TOKEN")
    client.connect()
    sub_id_1 = client.subscribe_to_attribute("frequency", callback)
    sub_id_2 = client.subscribe_to_all_attributes(callback)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        client.unsubscribe_from_attribute(sub_id_1)
        client.unsubscribe_from_attribute(sub_id_2)
        client.disconnect()


if __name__ == '__main__':
    main()
