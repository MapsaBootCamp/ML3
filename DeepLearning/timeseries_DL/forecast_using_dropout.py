import matplotlib.pyplot as plt
if True:
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
from pathlib import Path
import tensorflow as tf

from data_analysis import data_to_numpy
from data_prepare import normalize_data_params, dataset_from_array


fname = Path("data") / "jena_climate_2009_2016.csv"
raw_data, temperature = data_to_numpy(fname)

num_train_samples = int(0.5 * len(raw_data))
num_val_samples = int(0.25 * len(raw_data))
num_test_samples = len(raw_data) - num_train_samples - num_val_samples

mean, std = normalize_data_params(raw_data[:num_train_samples])

raw_data -= mean
raw_data /= std

sampling_rate = 6
sequence_length = 120
delay = sampling_rate * (sequence_length + 24 - 1)
batch_size = 256
train_dataset = dataset_from_array(
    raw_data, temperature, sampling_rate, sequence_length, delay, batch_size, 0, end_index=num_train_samples)
val_dataset = dataset_from_array(raw_data, temperature, sampling_rate,
                                 sequence_length, delay, batch_size, num_train_samples, end_index=num_train_samples + num_val_samples)
test_dataset = dataset_from_array(raw_data, temperature, sampling_rate,
                                  sequence_length, delay, batch_size, num_train_samples + num_val_samples)


print(raw_data.shape)


inputs = tf.keras.Input(shape=(sequence_length, raw_data.shape[-1]))
"""
In 2016, Yarin Gal, as part of his PhD
thesis on Bayesian deep learning, 5 determined the proper way to use dropout with a
recurrent network: the same dropout mask (the same pattern of dropped units)
should be applied at every timestep, instead of using a dropout mask that varies ran-
domly from timestep to timestep
"""
x = tf.keras.layers.LSTM(32, recurrent_dropout=0.25)(inputs)
# To regularize the Dense layer, we also add a Dropout layer after the LSTM.
x = tf.keras.layers.Dropout(0.5)(x)
outputs = tf.keras.layers.Dense(1)(x)
model = tf.keras.Model(inputs, outputs)

# inputs = tf.keras.Input(shape=(sequence_length, raw_data.shape[-1]))
# x = tf.keras.layers.GRU(32, return_sequences=True, recurrent_dropout=0.5)(inputs)
# x = tf.keras.layers.GRU(32, recurrent_dropout=0.5)(x)
# x = tf.keras.layers.Dropout(0.5)(x)
# outputs = tf.keras.layers.Dense(1)(x)
# model = tf.keras.Model(inputs, outputs)

print(model.summary())

callbacks = [tf.keras.callbacks.ModelCheckpoint(
    "jena_lstm.keras", save_best_only=True)]
model.compile(optimizer="adam", loss="mse", metrics=["mae"])
history = model.fit(train_dataset,
                    epochs=50,
                    validation_data=val_dataset,
                    callbacks=callbacks)
model = tf.keras.models.load_model("jena_lstm.keras")
print(f"Test MAE: {model.evaluate(test_dataset)[1]:.2f}")


loss = history.history["mae"]
val_loss = history.history["val_mae"]
epochs = range(1, len(loss) + 1)
plt.figure()
plt.plot(epochs, loss, "bo", label="Training MAE")
plt.plot(epochs, val_loss, "b", label="Validation MAE")
plt.title("Training and validation MAE")
plt.legend()
plt.show()
