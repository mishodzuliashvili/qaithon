import numpy as np

def kmeans(image, k=3, max_iter=100):
    data = image.reshape(-1, 3).astype(np.float32)

    centroids = data[np.random.choice(data.shape[0], k, replace=False)]

    for _ in range(max_iter):
        distances = np.linalg.norm(data[:, None] - centroids, axis=-1)

        labels = np.argmin(distances, axis=-1)

        centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])

    quantized_image = centroids[labels].reshape(image.shape).astype(np.uint8)

    return quantized_image