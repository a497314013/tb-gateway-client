

import time
import logging
from tb_gateway_mqtt import TBGatewayMqttClient

logging.basicConfig(level=logging.INFO)


attributes = {"atr1": 1, "atr2": True, "atr3": "value3"}
telemetry_simple = {"ts": int(round(time.time() * 1000)), "values": {"key1": "11"}}
telemetry_array = [
    {"ts": int(round(time.time() * 1000)), "values": {"key1": "11"}},
    {"ts": int(round(time.time() * 1000)), "values": {"key2": "22"}}
]


def main():
    gateway = TBGatewayMqttClient("127.0.0.1", username="TEST_GATEWAY_TOKEN")
    # without device connection it is impossible to get any messages
    gateway.connect()

    gateway.gw_send_telemetry("Test Device A2", telemetry_simple)
    gateway.gw_send_telemetry("Test Device A2", telemetry_array)
    gateway.gw_send_attributes("Test Device A2", attributes)
    gateway.disconnect()


if __name__ == '__main__':
    main()
