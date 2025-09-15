

import logging.handlers
import time

from tb_gateway_mqtt import TBGatewayMqttClient
try:
    import psutil
except ImportError:
    print("Please install psutil using 'pip install psutil' command")
    exit(1)
logging.basicConfig(level=logging.INFO)


def rpc_request_response(gateway, request_body):
    # request body contains id, method and other parameters
    logging.info(request_body)
    method = request_body["data"]["method"]
    device = request_body["device"]
    req_id = request_body["data"]["id"]
    # dependently of request method we send different data back
    if method == 'getCPULoad':
        gateway.gw_send_rpc_reply(device, req_id, psutil.cpu_percent(interval=0.1))
    elif method == 'getMemoryLoad':
        gateway.gw_send_rpc_reply(device, req_id, psutil.virtual_memory().percent)
    else:
        print('Unknown method: ' + method)


def main():
    gateway = TBGatewayMqttClient("127.0.0.1", username="TEST_GATEWAY_TOKEN")
    gateway.connect()
    # now rpc_request_response will process rpc requests from servers
    gateway.gw_set_server_side_rpc_request_handler(rpc_request_response)
    # without device connection it is impossible to get any messages
    gateway.gw_connect_device("Test Device A2", "default")
    try:
        # Waiting for the callback
        while not gateway.stopped:
            time.sleep(1)
    except KeyboardInterrupt:
        gateway.disconnect()
        gateway.stop()


if __name__ == '__main__':
    main()
