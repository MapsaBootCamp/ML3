if True:
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from pathlib import Path
import tensorflow as tf
import numpy as np
from typing import Tuple
from data_analysis import data_to_numpy


def normalize_data_params(data: np.ndarray) -> Tuple:
    if not isinstance(data, np.ndarray):
        raise TypeError("data should be numpy ndarray instance!")
    mean = data.mean(axis=0)
    std = data.std(axis=0)

    return mean, std


def dataset_from_array(X, y, sampling_rate, sequence_length, delay, batch_size, start_index, end_index=None):
    return tf.keras.utils.timeseries_dataset_from_array(
        X[:-delay],
        targets=y[delay:],
        sampling_rate=sampling_rate,
        sequence_length=sequence_length,
        shuffle=True,
        batch_size=batch_size,
        start_index=0,
        end_index=end_index)


"""
# Understanding timeseries_dataset_from_array()
int_sequence = np.arange(10)
# dummy_dataset = tf.keras.utils.timeseries_dataset_from_array(data=int_sequence[:-3],
#                                                              targets=int_sequence[3:], sequence_length=2, batch_size=2)
# for inputs, targets in dummy_dataset:
#     print(inputs)
#     for i in range(inputs.shape[0]):
#         print([int(x) for x in inputs[i]], int(targets[i]))


# alternative
dataset = tf.data.Dataset.from_tensor_slices(int_sequence[:-1]).window(
    4, shift=1, drop_remainder=True).flat_map(lambda window_ds: window_ds.batch(4)).map(lambda x: (x[:-1], x[-1])).batch(2)
for inputs, targets in dataset:
    for i in range(inputs.shape[0]):
        print([int(x) for x in inputs[i]], int(targets[i]))
# exit(0)

"""


# normalize_data(np.array([12, 14]))


if __name__ == "__main__":
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

    for samples, targets in test_dataset.take(1):
        print("samples shape:", samples.shape)
        print("targets shape:", targets.shape)
