from skimage.feature import peak_local_max
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(ncols=2, nrows=3,
                         figsize=(8, 4))
ax0, ax1, ax2, ax3, ax4, ax5  = axes.flat

coordinates = peak_local_max('D:\\HotTechnologies\\pythonimageprocessing\\shakeerpicnew.jpeg', min_distance=20)

ax3.imshow('D:\\HotTechnologies\\pythonimageprocessing\\shakeerpicnew.jpeg', cmap=plt.cm.gray)
ax3.autoscale(False)
ax3.plot(coordinates[:, 1],
         coordinates[:, 0], c='r.')
ax3.set_title('Peak local maxima', fontsize=24)
ax3.axis('off')