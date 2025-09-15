

import logging.handlers
import time

from tb_gateway_mqtt import TBGatewayMqttClient
logging.basicConfig(level=logging.INFO)


def callback(result):
    logging.info("Callback for attributes, %r", result)


def callback_for_everything(result):
    logging.info("Everything goes here, %r", result)


def callback_for_specific_attr(result):
    logging.info("Specific attribute callback, %r", result)


def main():
    gateway = TBGatewayMqttClient("127.0.0.1", username="TEST_GATEWAY_TOKEN")
    gateway.connect()
    # without device connection it is impossible to get any messages
    gateway.gw_connect_device("ImageTest")

    gateway.gw_subscribe_to_all_attributes(callback_for_everything)

    gateway.gw_subscribe_to_attribute("ImageTest", "image", callback_for_specific_attr)

    sub_id = gateway.gw_subscribe_to_all_device_attributes("ImageTest", callback)
    gateway.gw_unsubscribe(sub_id)

    try:
        # Waiting for the callback
        while not gateway.stopped:
            time.sleep(1)
    except KeyboardInterrupt:
        gateway.disconnect()
        gateway.stop()


if __name__ == '__main__':
    main()
