import GenerateData.create_2_breasts_image as create_2_breasts_image
from GenerateData import create_4_breasts_image
import GenerateData.save_images as save_images
import matplotlib.pyplot as plt


def run_deep(patients, path):
    for person in patients:
        fig = create_2_breasts_image.create(person.deep_left, person.deep_right)
        save_images.save(name='cls_' + str(person.cls) + '__s_type_' + str(person.sensor_type) +
                         '__id_' + str(person.id_person) + '__deep', cls=person.cls, path=path)
        plt.close(fig)


def run_skin(patients, path):
    for person in patients:
        fig = create_2_breasts_image.create(person.skin_left, person.skin_right)
        save_images.save(name='cls_' + str(person.cls) + '__s_type_' + str(person.sensor_type) +
                         '__id_' + str(person.id_person) + '__skin', cls=person.cls, path=path)
        plt.close(fig)


def run_all(patients, path):
    for person in patients:
        fig = create_4_breasts_image.create(person.deep_left, person.deep_right, person.skin_left, person.skin_right)
        save_images.save(name='cls_' + str(person.cls) + '__s_type_' + str(person.sensor_type) +
                         '__id_' + str(person.id_person) + '__all', cls=person.cls, path=path)
        plt.close(fig)
