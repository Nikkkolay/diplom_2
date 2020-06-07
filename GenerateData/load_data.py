from GenerateData.patient_data import Person
import csv


def load_data(path):
    patients = []
    _is_first_row = True
    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            if _is_first_row:
                _is_first_row = False
                continue
            patients.append(Person(row))
    return patients
