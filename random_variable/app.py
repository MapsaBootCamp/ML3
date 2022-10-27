from curses import ACS_GEQUAL
from statistics import variance
import numpy as np

normal_dis_data = np.random.normal(2, 5, 10000000)


print(sum(normal_dis_data) / len(normal_dis_data))
print(np.mean(normal_dis_data))