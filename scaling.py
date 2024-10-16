import numpy as np

IMG_URL = "qaioz.jpg"


def scale_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)

    scaled_image = np.zeros((height, width, image.shape[2]), dtype=np.uint8)

    row_scale = height / image.shape[0]
    col_scale = width / image.shape[1]

    # scale down
    if scale_percent < 100:
        row_scale = 1 / row_scale
        col_scale = 1 / col_scale

    for i in range(height):
        for j in range(width):
            orig_x = int(i / row_scale if scale_percent > 100 else i * row_scale)
            orig_y = int(j / col_scale if scale_percent > 100 else j * col_scale)
            scaled_image[i, j] = image[orig_x, orig_y]

    return scaled_image
