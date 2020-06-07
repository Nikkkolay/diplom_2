from keras.preprocessing.image import ImageDataGenerator
import os


class LoadImages:
    def __init__(self, batch_size, image_width, image_height,
                 train_dir, train_healthy_dir, train_sick_dir,
                 val_dir, val_healthy_dir, val_sick_dir,
                 test_dir, test_healthy_dir, test_sick_dir):

        self.batch_size = batch_size
        self.image_width = image_width
        self.image_height = image_height

        self.train_dir = train_dir
        self.train_healthy_dir = train_healthy_dir
        self.train_sick_dir = train_sick_dir
        self.num_healthy_train = len(os.listdir(self.train_healthy_dir))
        self.num_sick_train = len(os.listdir(self.train_sick_dir))
        self.total_train_num = self.num_healthy_train + self.num_sick_train

        self.val_dir = val_dir
        self.val_healthy_dir = val_healthy_dir
        self.val_sick_dir = val_sick_dir
        self.num_healthy_val = len(os.listdir(self.val_healthy_dir))
        self.num_sick_val = len(os.listdir(self.val_sick_dir))
        self.total_val_num = self.num_healthy_val + self.num_sick_val

        self.test_dir = test_dir
        self.test_healthy_dir = test_healthy_dir
        self.test_sick_dir = test_sick_dir
        self.num_healthy_test = len(os.listdir(self.test_healthy_dir))
        self.num_sick_test = len(os.listdir(self.test_sick_dir))
        self.total_test_num = self.num_healthy_test + self.num_sick_test

    def get_train_data(self):
        train_image_generator = ImageDataGenerator(rescale=1. / 255)
        train_data_gen = train_image_generator.flow_from_directory(batch_size=self.batch_size,
                                                                   directory=self.train_dir,
                                                                   shuffle=True, class_mode='binary',
                                                                   target_size=(self.image_width, self.image_height))
        return train_data_gen

    def get_validate_data(self):
        validation_image_generator = ImageDataGenerator(rescale=1. / 255)
        val_data_gen = validation_image_generator.flow_from_directory(batch_size=self.batch_size,
                                                                      directory=self.val_dir,
                                                                      shuffle=False, class_mode='binary',
                                                                      target_size=(self.image_width, self.image_height))
        return val_data_gen

    def get_test_data(self):
        test_image_generator = ImageDataGenerator(rescale=1. / 255)
        test_data_gen = test_image_generator.flow_from_directory(batch_size=self.batch_size,
                                                                 directory=self.test_dir,
                                                                 shuffle=False, class_mode='binary',
                                                                 target_size=(self.image_width, self.image_height))
        return test_data_gen
