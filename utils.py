import numpy as np
from PIL import Image

IMG_SIZE = (224,224)

def preprocess_image(path):

    image = Image.open(path)

    image = image.convert("RGB")

    image = image.resize(IMG_SIZE)

    image = np.array(image,dtype=np.float32)

    image = np.expand_dims(image,0)

    return image