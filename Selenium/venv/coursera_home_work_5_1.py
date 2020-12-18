import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self._host = host
        self._port = port
        self._timeout = timeout
        try:
            self._sock = socket.create_connection((self._host, self._port), self._timeout)
        except socket.error:
            raise ClientError

    def put(self, name_serv, count_serv, timestamp=None):
        stamp = timestamp or int(time.time())
        send_data = f'put {name_serv} {count_serv} {stamp}\n'.encode('utf-8')

        try:
            self._sock.send(send_data)
            response = self._sock.recv(1024)
            if b'ok\n' not in response:
                raise ClientError
        except Exception:
            raise ClientError

    def get(self, name_metric=None):
        response_dict = {}
        try:
            send_key = f'get {name_metric}\n'.encode('utf-8')
            self._sock.send(send_key)
            response = self._sock.recv(1024).decode('utf-8')
            response = response.strip('\\\n').split('\n')
            print(response)
            if 'ok' != response[0]:
                raise ClientError
            del response[0]
            for element in response:
                element = element.split(' ')
                if len(element) != 3:
                    raise ClientError
                else:
                    for el in element:
                        if el is None:
                            raise ClientError
                    key = element[0]
                    val_1 = float(element[1])
                    val_2 = int(element[2])
                    append_data = []
                    if key in response_dict:
                        append_data = (response_dict[key])
                        append_data.append((val_2, val_1))
                        append_data = list(sorted(append_data))
                    else:
                        append_data.append((val_2, val_1))

                    response_dict[key] = append_data
            return response_dict
        except Exception:
            raise ClientError

#
# client = Client('127.0.0.1', 8888)
# print(client.get('*'))
# print(client.put('qwerty', 0.8))
