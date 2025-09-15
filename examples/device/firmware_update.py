

import time
import logging
from tb_device_mqtt import TBDeviceMqttClient, FW_STATE_ATTR

logging.basicConfig(level=logging.INFO)


def main():
    client = TBDeviceMqttClient("127.0.0.1", username="A2_TEST_TOKEN")
    client.connect()

    client.get_firmware_update()

    # Waiting for firmware to be delivered
    while not client.current_firmware_info[FW_STATE_ATTR] == 'UPDATED':
        time.sleep(1)

    client.disconnect()
    client.stop()


if __name__ == '__main__':
    main()
