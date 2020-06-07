import numpy as np


class Person:
    def __init__(self, csv_list):
        self.id_person = int(csv_list[0])
        self.sensor_type = int(csv_list[1])
        self.cls = int(csv_list[-1])

        temperatures = []
        start = 2
        try:
            for i in range(start, start + 10):
                temperatures.append(float(csv_list[i]))
            self.deep_right = np.array(temperatures)
            start += 10
            temperatures = []

            for i in range(start, start + 10):
                temperatures.append(float(csv_list[i]))
            self.deep_left = np.array(temperatures)
            start += 10
            temperatures = []

            for i in range(start, start + 10):
                temperatures.append(float(csv_list[i]))
            self.skin_right = np.array(temperatures)
            start += 10
            temperatures = []

            for i in range(start, start + 10):
                temperatures.append(float(csv_list[i]))
            self.skin_left = np.array(temperatures)
        except:
            print("в id " + csv_list[0] + ' проблема')
