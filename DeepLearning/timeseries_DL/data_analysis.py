from matplotlib import pyplot as plt
import numpy as np
from pathlib import Path
from datetime import datetime


def read_data(fname):
    with open(fname) as f:
        data = f.read()
    return data


def data_to_numpy(fname):
    with open(fname) as f:
        data = f.read()

    lines = data.split("\n")
    header = lines[0].split(",")
    lines = lines[1:]

    temperature = np.zeros((len(lines),))
    raw_data = np.zeros((len(lines), len(header) - 1))

    for i, line in enumerate(lines):
        values = [float(x) for x in line.split(",")[1:]]
        temperature[i] = values[1]
        raw_data[i, :] = values[:]

    return raw_data, temperature


def train_test_val_split(X, y, train_size, val_size):
    num_train_samples = int(train_size * len(X))
    num_val_samples = int(val_size * len(X))
    train = (X[:num_train_samples], y[:num_train_samples])
    val = (X[num_train_samples:num_val_samples + num_train_samples],
           y[num_train_samples: num_val_samples + num_train_samples])
    test = (X[num_val_samples + num_train_samples:],
            y[num_val_samples + num_train_samples:])
    return train, val, test


if __name__ == "__main__":
    fname = Path("data") / "jena_climate_2009_2016.csv"

    data = read_data(fname)
    lines = data.split("\n")
    header = lines[0].split(",")
    lines = lines[1:]

    print("headers: \n", header)
    print("\ndata length: ", len(lines))
    time_step = (datetime.strptime(lines[1].split(",")[
        0], "%d.%m.%Y %H:%M:%S") - datetime.strptime(lines[0].split(",")[0], "%d.%m.%Y %H:%M:%S")).seconds
    print("time step: ", time_step / 60, " minutes")

    raw_data, temperature = data_to_numpy(fname)
    plt.plot(range(len(temperature)), temperature)
    plt.show()

    plt.figure()
    plt.title("Temperature over the first 10 days of the dataset (ºC)")
    plt.plot(range(1440), temperature[:1440])
    plt.show()
