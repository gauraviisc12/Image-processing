import os
import cv2
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

specified_strings = ["008_2022-11-03-15-11-30", "012_2022-11-10-16-25-06", "007_2022-11-02-17-35-40",
                      "041_2022-11-17-15-04-53", "044_2022-11-17-15-11-13", "045_2022-11-17-15-13-30",
                      "042_2022-11-17-15-08-53"]

x_vals = []
y_vals = []

for ele in specified_strings:
    x_vals.append(np.load(f"video_{ele}_x.npy"))
    y_vals.append(np.load(f"video_{ele}_y.npy"))


fig = plt.figure()
ax1 = fig.add_subplot(111)

for idx, ele in enumerate(specified_strings):
    l = f"{x_vals[idx].shape[0]}"
    print("@@@@", l)
    ax1.scatter(x_vals[idx], y_vals[idx], label=l)
    ax1.set_xlabel('Percentage predicted area')
    ax1.set_ylabel('IOU')

plt.legend()
plt.savefig("res5.png")

