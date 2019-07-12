import keras
from keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import sklearn
import cv2
import os
import keras
from keras.models import Sequential, Input, Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU
import PIL







def construct_model(num_classes):
    fashion_model = Sequential()
    fashion_model.add(Conv2D(64, kernel_size=(3, 3), activation='linear', input_shape=(300, 300, 1), padding='same'))
    fashion_model.add(LeakyReLU(alpha=0.1))
    fashion_model.add(MaxPooling2D((2, 2), padding='same'))
    fashion_model.add(Conv2D(128, (3, 3), activation='linear', padding='same'))
    fashion_model.add(LeakyReLU(alpha=0.1))
    fashion_model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
    fashion_model.add(Conv2D(256, (3, 3), activation='linear', padding='same'))
    fashion_model.add(LeakyReLU(alpha=0.1))
    fashion_model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
    fashion_model.add(Flatten())
    fashion_model.add(Dense(256, activation='linear'))
    fashion_model.add(LeakyReLU(alpha=0.1))
    fashion_model.add(Dense(num_classes, activation='softmax'))

    fashion_model.compile(loss='categorical_crossentropy', optimizer=keras.optimizers.Adam(),
                          metrics=['accuracy'])
    fashion_model.summary()
    return fashion_model


def main():
    ## parameters
    num_classes = 5
    batch_size = 64
    epochs = 20

    datagen = ImageDataGenerator(
        featurewise_center=True,
        featurewise_std_normalization=True,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True)

    train_datagen = ImageDataGenerator(
        shear_range=0.2,
        zoom_range=0.2,
        validation_split=0.1,
        horizontal_flip=True)

    train_generator = train_datagen.flow_from_directory(
        'E:\Kaggle\\500data',
        target_size=(300, 300),
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical')

    # test_datagen = ImageDataGenerator(rescale=1. / 255)
    # validation_generator = test_datagen.flow_from_directory(
    #     'data/validation',
    #     target_size=(150, 150),
    #     batch_size=32,
    #     class_mode='binary')

    # Construct model
    model = construct_model(num_classes)
    model.fit_generator(
        train_generator, steps_per_epoch=100, epochs=20,
    )

    return


if __name__ == '__main__':
    main()
