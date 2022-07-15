import os

# Defining our paths for training and validation steps
train_dir = '/home/htriedman/nsfw_data_scraper/data/train/'
validation_dir = '/home/htriedman/nsfw_data_scraper/data/validate/'

# Target image dimensions
dimension1, dimension2, dimension3 = 224, 224, 3
# For training
batch_size = 30

''' For "content-filtration-model.py" '''

# callback Stop_Validation
stopping_acc = 0.9600
stopping_loss = 0.1000

# callback callback_reduce_lr
monitor = 'val_loss'
factor = 0.2
patience = 5
min_lr = 0.0001

# For Adam optimizer
learning_rate = 0.0001
loss = 'categorical_crossentropy'
metrics = ['accuracy']

unsafe_images_train = [fn for fn in os.listdir('/home/htriedman/nsfw_data_scraper/data/train/nsfw/')]
safe_images_train = [fn for fn in os.listdir('/home/htriedman/nsfw_data_scraper/data/train/sfw/')]
unsafe_images_validation = [fn for fn in os.listdir('/home/htriedman/nsfw_data_scraper/data/validate/nsfw/')]
safe_images_validation = [fn for fn in os.listdir('/home/htriedman/nsfw_data_scraper/data/validate/sfw/')]

num_training_images = len(unsafe_images_train+safe_images_train)
num_validation_images = len(unsafe_images_validation+safe_images_validation)

epochs = 25
