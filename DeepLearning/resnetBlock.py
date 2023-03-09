import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Sequential
CUDA_VISIBLE_DEVICES = ""


# print(tf.__version__)

inputs = keras.Input(shape=(32, 32, 3))
x = layers.Rescaling(1./255)(inputs)


def res_block(x, number_conv, number_filter, max_pool=False, batch_norm=True):
    residual = x
    for i in range(number_conv):
        if not batch_norm:
            x = layers.Conv2D(number_filter, 3, padding="same")(x)
        else:
            x = layers.Conv2D(number_filter, 3,
                              padding="same", use_bias=False)(x)
            x = layers.BatchNormalization()(x)
            x = layers.Activation("relu")(x)
    if (max_pool):
        x = layers.MaxPooling2D(2, padding="same")(x)
        residual = layers.Conv2D(
            number_filter, 1, strides=2, padding="same")(residual)
    else:
        residual = layers.Conv2D(number_filter, 1, padding="same")(residual)
    return layers.add([x, residual])


x = res_block(x, 2, 32)
x = res_block(x, 3, 64)
x = res_block(x, 3, 128, max_pool=True)


x = layers.GlobalAveragePooling2D()(x)
outputs = layers.Dense(1, activation="sigmoid")(x)
model = keras.Model(inputs=inputs, outputs=outputs)
model.summary()
