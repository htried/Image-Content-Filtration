# Extracting safe images from Lorem Picsum
import random
import requests

# importing under-definable constants
from constants_scraper_safe import (
    lowest_dimension,
    highest_dimension,
    number_of_images
)

for i in range(number_of_images):
    # Create custom URL
    SFW_image_generator = f"https://picsum.photos/{random.randint(lowest_dimension, highest_dimension)}/{random.randint(lowest_dimension, highest_dimension)}"
    response = requests.get(SFW_image_generator)
    file = open(f"datasets/sfw/image_{i+4471}.jpg", "wb")
    file.write(response.content)
    file.close()
