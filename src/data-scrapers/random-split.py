import os
import shutil
from sklearn.model_selection import train_test_split

sfw = os.listdir('/home/htriedman/Image-Content-Filtration/datasets/sfw')
nsfw = os.listdir('/home/htriedman/Image-Content-Filtration/datasets/nsfw')

train_sfw, test_sfw = train_test_split(sfw, test_size=0.2)
train_nsfw, test_nsfw = train_test_split(nsfw, test_size=0.2)

for f in train_sfw:
  shutil.copy2(f'/home/htriedman/Image-Content-Filtration/datasets/sfw/{f}', f'/home/htriedman/Image-Content-Filtration/datasets/train/sfw/{f}')

for f in train_nsfw:
  shutil.copy2(f'/home/htriedman/Image-Content-Filtration/datasets/nsfw/{f}', f'/home/htriedman/Image-Content-Filtration/datasets/train/nsfw/{f}')

for f in test_sfw:
  shutil.copy2(f'/home/htriedman/Image-Content-Filtration/datasets/sfw/{f}', f'/home/htriedman/Image-Content-Filtration/datasets/validate/sfw/{f}')

for f in test_nsfw:
  shutil.copy2(f'/home/htriedman/Image-Content-Filtration/datasets/nsfw/{f}', f'/home/htriedman/Image-Content-Filtration/datasets/validate/nsfw{f}')
