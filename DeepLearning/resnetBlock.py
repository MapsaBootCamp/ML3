import tensorflow as tf

CUDA_VISIBLE_DEVICES = ""


# print(tf.__version__)

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

inputs = tf.keras.Input(shape=(32, 32, 3))
x = tf.keras.layers.Rescaling(1./255)(inputs)


def res_block(x, number_conv, number_filter, max_pool=False, batch_norm=True):
    residual = x
    for i in range(number_conv):
        if not batch_norm:
            x = tf.keras.layers.Conv2D(
                number_filter, 3, padding="same", activation="relu")(x)
        else:
            x = tf.keras.layers.Conv2D(
                number_filter, 3, padding="same", use_bias=False)(x)
            x = tf.keras.layers.BatchNormalization()(x)
            x = tf.keras.layers.Activation("relu")(x)
    if (max_pool):
        x = tf.keras.layers.MaxPooling2D(2, padding="same")(x)
        residual = tf.keras.layers.Conv2D(
            number_filter, 1, strides=2, padding="same")(residual)
    else:
        residual = tf.keras.layers.Conv2D(
            number_filter, 1, padding="same")(residual)
    x = tf.keras.layers.add([x, residual])
    return x


x = res_block(x, 2, 32)
x = res_block(x, 3, 64)
x = res_block(x, 3, 128, max_pool=True)


x = tf.keras.layers.GlobalAveragePooling2D()(x)
outputs = tf.keras.layers.Dense(10, activation="softmax")(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)
# model.summary()
model.compile(loss=tf.keras.losses.sparse_categorical_crossentropy,
              metrics=[tf.keras.metrics.sparse_categorical_accuracy],
              optimizer="sgd")
model.fit(x_train, y_train, epochs=20, batch_size=32, validation_split=0.2)
