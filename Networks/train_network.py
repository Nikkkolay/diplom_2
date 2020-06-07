import Networks.network_snn_1 as network
from Networks.load_images import LoadImages
import numpy as np
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt

load_images = LoadImages(
    batch_size=100, image_width=network.IMAGE_WIDTH, image_height=network.IMAGE_HEIGHT,
    train_dir='samples/sample_1/train',
    train_healthy_dir='samples/sample_1/train/0',
    train_sick_dir='samples/sample_1/train/1',
    val_dir='samples/sample_1/val',
    val_healthy_dir='samples/sample_1/val/0',
    val_sick_dir='samples/sample_1/val/1',
    test_dir=None,
    test_healthy_dir=None,
    test_sick_dir=None
)

checkpoint = ModelCheckpoint("model_1_weights.hdf5", monitor='acc', mode='max', save_best_only=True, verbose=1)


EPOCHS = 100
# BATCH_SIZE = 100  # количество тренировочных изображений для обработки перед обновлением параметров модели

history = network.model.fit_generator(
    load_images.get_train_data(),
    steps_per_epoch=int(np.ceil(load_images.total_train_num / float(load_images.batch_size))),
    epochs=EPOCHS,
    validation_data=load_images.get_validate_data(),
    validation_steps=int(np.ceil(load_images.total_val_num / float(load_images.batch_size))),
    callbacks=[checkpoint]
)

acc = history.history['acc']
val_acc = history.history['val_acc']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(EPOCHS)


plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Точность на обучении')
plt.plot(epochs_range, val_acc, label='Точность на валидации')
plt.legend(loc='lower right')
plt.title('Точность на обучающих и валидационных данных')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Потери на обучении')
plt.plot(epochs_range, val_loss, label='Потери на валидации')
plt.legend(loc='upper right')
plt.title('Потери на обучающих и валидационных данных')
plt.savefig('./foo.png')
plt.show()
