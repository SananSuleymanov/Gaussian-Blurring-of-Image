
"""
@author: Sanan Suleymanov
"""
import cv2
import matplotlib.pyplot as plt
import gaussian


image_y = cv2.imread("mountain.jpg", cv2.IMREAD_GRAYSCALE)

g = gaussian.gaussian_blur(image_y)
result = g.gaus(4.0)

fig = plt.figure(figsize=(10,7))
fig.add_subplot(1,2, 1)
plt.imshow(image_y, cmap="gray")
fig.add_subplot(1,2, 2)

plt.imshow(result, cmap="gray")