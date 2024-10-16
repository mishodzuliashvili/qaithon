from scaling import scale_image
import cv2
import matplotlib.pyplot as plt
from kmeans import kmeans

IMG_URL = "qaioz.jpg"
image = cv2.imread(IMG_URL)

scaled_down_image = scale_image(image, 50)
scaled_up_image = scale_image(image, 120)
quantized_image = kmeans(scaled_down_image, k=5)

_, axes = plt.subplots(2, 3)

IMAGES = [
    {"image": image, "title": "Original Image"},
    {"image": scaled_down_image, "title": "Scaled Down Image"},
    {"image": scaled_up_image, "title": "Scaled Up Image"},
    {"image": quantized_image, "title": "Quantized Image"},
]

for i, img in enumerate(IMAGES):
    axes[i // 3, i % 3].imshow(cv2.cvtColor(img["image"], cv2.COLOR_BGR2RGB))
    axes[i // 3, i % 3].set_title(img["title"])
    axes[i // 3, i % 3].axis("off")

plt.tight_layout()
plt.show()
