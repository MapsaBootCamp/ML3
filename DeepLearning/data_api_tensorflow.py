if True:
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf


### filter, map, batch, ...

data = [8, 19, 3, -20, 12, 46, 72, 80]
tf_dataset = tf.data.Dataset.from_tensor_slices(data)

# for val in tf_dataset:
#     # print(val)
#     print(val.numpy())


# for val in tf_dataset.filter(lambda x: x > 0):
#     print(val.numpy())

for val in tf_dataset.map(lambda x: x * 2).take(2):
    print(val.numpy())

# for val in tf_dataset.batch(2):
#     print(val.numpy())


# tf_dataset = tf_dataset.filter(lambda x: x > 0).map(lambda y: y*2).batch(2)
# for val in tf_dataset.as_numpy_iterator():
#     print(val)

# read data from directory
# dataset_from_dir = tf.data.Dataset.list_files('path/*', shuffle=False)
