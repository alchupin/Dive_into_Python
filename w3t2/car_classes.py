import os
import csv

class BaseCar():
    def __init__(self, car_type, photo_file_name, brand, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying
        
    def get_foto_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)[-1][1:]
        return ext
        
        
class Car(BaseCar):
    def __init__(self, car_type, photo_file_name, brand, carrying, passenger_seats_count):
        
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying
        self.car_type = 'car'
        self.passenger_seats_count = passenger_seats_count
        
        
class Truck(BaseCar):
    def __init__(self, car_type, photo_file_name, carrying, brand, body_whl):
        
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying
        self.car_type = 'truck'
        if len(body_whl>0):
            self.body_width = body_whl.split('x')[0]
            self.body_height = body_whl.split('x')[1]
            self.body_length = body_whl.split('x')[2]
    
    def get_body_volume(self):
        body_volume = self.body_width * self.body_height * self.body_length
        return body_volume
        
    
class SpecMachine(BaseCar):
    def __init__(self, car_type, photo_file_name, brand, carrying, extra):
        
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying
        self.car_type = 'spec_machine'
        self.extra = extra

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as f:
        data = csv.reader(f, delimiter=';')
        next(data)
        for row in data:
            if len(row)>0:
                if row[0] == 'car':
                    car_list.append('car')
                if row[0] == 'truck':
                    car_list.append('truck')
                if row[0] == 'spec_machine':
                    car_list.append('spec_machine')
                
                
    return car_list

if __name__ == '__main__':
    get_car_list('coursera_week3_cars.csv')
'''

my_car = Car('truck', 'kia.jpeg', 'kia', '1500', '5')
print(my_car.car_type)
print(my_car.get_foto_file_ext())
'''
