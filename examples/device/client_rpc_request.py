

import time
import logging
from tb_device_mqtt import TBDeviceMqttClient
logging.basicConfig(level=logging.INFO)


def callback(request_id, resp_body, exception=None):
    if exception is not None:
        logging.error("Exception: " + str(exception))
    else:
        logging.info("request id: {request_id}, response body: {resp_body}".format(request_id=request_id,
                                                                                   resp_body=resp_body))


def main():
    client = TBDeviceMqttClient("127.0.0.1", username="A2_TEST_TOKEN")

    client.connect()
    # call "getTime" on server and receive result, then process it with callback
    client.send_rpc_call("getTime", {}, callback)
    try:
        while not client.stopped:
            time.sleep(1)
    except KeyboardInterrupt:
        client.disconnect()
        client.stop()


if __name__ == '__main__':
    main()
