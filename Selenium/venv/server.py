# # Неделя 3 задание по классам
# # import os.path
# # import csv
# #
# #
# # class CarBase:
# #     def __init__(self, brand, photo_file_name, carrying):
# #         try:
# #             # self.car_type = car_type
# #             # if car_type not in ['car', 'truck', 'spec_machine']:
# #             #     raise TypeError
# #             self.photo_file_name = photo_file_name
# #             self.ext = os.path.splitext(photo_file_name)[1]
# #             if self.ext not in ['.jpg', '.jpeg', '.png', '.gif']:
# #                 raise TypeError
# #             self.brand = brand
# #             self.carrying = float(carrying)
# #         except TypeError:
# #             pass
# #         # else:
# #         #     self.car_type = car_type
# #
# #     def get_photo_file_ext(self):
# #         return self.ext
# #
# #
# # class Car(CarBase):
# #     def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
# #         self.passenger_seats_count = int(passenger_seats_count)
# #         self.car_type = self.__class__.__name__.lower()
# #         super().__init__(brand, photo_file_name, carrying)
# #
# #
# # class Truck(CarBase):
# #     def __init__(self, brand, photo_file_name, carrying, body_whl):
# #         self.car_type = self.__class__.__name__.lower()
# #         super().__init__(brand, photo_file_name, carrying)
# #         try:
# #             self.body_length, self.body_width, self.body_height = map(float, body_whl.split('x'))
# #         except ValueError:
# #             self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0
# #
# #     def get_body_volume(self):
# #         return self.body_length * self.body_width * self.body_height
# #
# #
# # class SpecMachine(CarBase):
# #     def __init__(self, brand, photo_file_name, carrying, extra):
# #         super().__init__(brand, photo_file_name, carrying)
# #         self.extra = extra
# #         self.car_type = 'spec_machine'
# #
# #
# # def get_car_list(csv_filename):
# #     car_list = []
# #     with open(csv_filename, encoding='utf-8') as csv_fd:
# #         reader = csv.reader(csv_fd, delimiter=';')
# #         next(reader)
# #         for row in reader:
# #
# #             try:
# #                 car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
# #                 if not brand or not photo_file_name or not carrying:
# #                     continue
# #
# #                 if os.path.splitext(photo_file_name)[1] not in ['.jpg', '.jpeg', '.png', '.gif']:
# #                     print(os.path.splitext(photo_file_name)[1])
# #                     continue
# #                 if car_type == 'car':
# #                     if not passenger_seats_count:
# #                         continue
# #                     car = Car(brand, photo_file_name, carrying, passenger_seats_count)
# #
# #                 elif car_type == 'truck':
# #
# #                     car = Truck(brand, photo_file_name, carrying, body_whl)
# #
# #                 elif car_type == 'spec_machine':
# #                     if not extra:
# #                         continue
# #                     car = SpecMachine(brand, photo_file_name, carrying, extra)
# #                 else:
# #                     continue
# #                 car_list.append(car)
# #             except ValueError:
# #                 continue
# #             except UnboundLocalError:
# #                 continue
# #
# #     return car_list
# #
# #
# # # car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
# # # print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
# #
# # # cars = get_car_list('cars.csv')
# # # print(len(cars))
# # # for car in cars:
# # #     print(type(car))
# from string import ascii_letters
#
# # Home work 'magic methods'
# # import tempfile
# # import os.path
# # import uuid
# #
# #
# # class File:
# #     def __init__(self, path):
# #         self.path = os.path.join(tempfile.gettempdir(), path)
# #         if not os.path.isfile(self.path):
# #             open(self.path, 'w').close()
# #         self.current_position = 0
# #
# #     def read(self):
# #         with open(self.path, 'r') as file:
# #             f = file.read()
# #             return f
# #
# #     def write(self, srting):
# #         with open(self.path, 'w') as file:
# #             file.write(srting)
# #             print(len(srting))
# #
# #     def __add__(self, other):
# #         sum_file = os.path.join(tempfile.gettempdir(), str(uuid.uuid1()))
# #         new = type(self)(sum_file)
# #         new.write((self.read() + other.read()))
# #         return new
# #
# #     def __str__(self):
# #         return self.path
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
# #         with open(self.path, 'r') as file:
# #             file.seek(self.current_position)
# #             lines = file.readline()
# #             self.len_file = len(lines)
# #             if not lines:
# #                 self.current_position = 0
# #                 raise StopIteration
# #             self.current_position = file.tell()
# #             return lines
# #
# #
# #
# #
# # path_to_file = 'test'
# # file = File(path_to_file)
# # file1 = File(path_to_file + '_1')
# # file2 = File(path_to_file + '_2')
# # file1.write('123\n')
# # file2.write('456\n')
# #
# # file3 = file1 + file2
# # print(file3)
# # print(isinstance(file3, File))
# #
# # for line in file3:
# #     print(ascii(line))
# # for line in file3:
# #     print('1', ascii(line))
# # print(str(uuid.uuid1()))
# # Home work 'work with Descriptors'
# # class Value:
# #     def __init__(self):
# #         self.amount = None
# #
# #     def __get__(self, instance, owner):
# #         return self.amount
# #
# #     def __set__(self, instance, value):
# #         self.amount = int(value - (value * instance.commission))
# #         return self.amount
# #
# #
# # class Accaunt:
# #     amount = Value()
# #
# #     def __init__(self, commission):
# #         self.commission = commission
# #
# #
# #
# # new_account = Accaunt(0.2)
# # print(new_account.commission)
# # new_account.amount = 200
# # print(new_account.amount)
# #
# # Метаклассы
# # class A(type):
# #     def __new__(cls, name, parents, attrs):
# #         if 'class_id' not in attrs:
# #             attrs['class_id'] = name.lower()
# #         return super().__new__(cls, name, parents, attrs)
# #
# #
# # class B(metaclass=A):
# #     def __str__(self):
# #         return 'J'
# #
# #
# # class Open_my:
# #     def __init__(self):
# #         self.f = open('r.txt', 'r')
# #     def __enter__(self):
# #         print('as')
# #         return self.f
# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         self.f.close()
# #
# # with Open_my() as f:
# #     pass
# # Тест астеройд
# # import json
# # import unittest
# # import requests
# # from unittest.mock import patch
# #
# #
# # class Asteroid:
# #     BASE_API_URL = 'https://api.nasa.gov/neo/rest/v1/neo/{}?api_key=DEMO_KEY'
# #
# #     def __init__(self, spk_id):
# #         self.api_url = self.BASE_API_URL.format(spk_id)
# #
# #     def get_data(self):
# #         return requests.get(self.api_url).json()
# #
# #     @property
# #     def name(self):
# #         return self.get_data()['name']
# #
# #     @property
# #     def diameter(self):
# #         return int(self.get_data()['estimated_diameter']['meters']['estimated_diameter_max'])
# #
# #
# # ast = Asteroid(2099942)
# #
# #
# # class TestAsteroid(unittest.TestCase):
# #     def SetUp(self):
# #         self.asteroid = Asteroid(2099942)
# #
# #     def mocked_get_data(self):
# #         return self.asteroid.get_data()
# #
# #     # @patch('asteroid.Asteroid.get_data', mocked_get_data)
# #     def test_name(self):
# #         self.assertEqual(
# #             self.asteroid.get_data()['name'], '99942 Apophis (2004 MN4)'
# #         )
# #
# #     def test_diameter(self):
# #         self.assertEqual(
# #             self.asteroid.diameter, 682
# #         )
# реализация сервера для тестирования метода get по заданию - Клиент для отправки метрик
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8888))
sock.listen(1)
conn, addr = sock.accept()

print('Соединение установлено:', addr)

# переменная response хранит строку возвращаемую сервером, если вам для
# тестирования клиента необходим другой ответ, измените ее
response = b'ok\npalm.cpu 10.5 1601864247\neardrum.cpu 15.3 1501864259\npalm.cpu 8.3 1501864340\neardrum.memory 200 1501861111\n\n'

while True:
    data = conn.recv(1024)
    if not data:
        break
    request = data.decode('utf-8')
    print(f'Получен запрос: {ascii(request)}')
    print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
    conn.send(response)

conn.close()