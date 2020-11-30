#Usage
# python train_test_split.py
import os
import config
import shutil
import random

class DataSpliter ():

  def buildDataset(self, imagesPath, dtype):
    try:
      path = os.path.join(config.BASE_PATH, dtype)

      if os.path.isdir(path):
        shutil.rmtree(path)

      if not os.path.isdir(path):
        os.mkdir(path)

      for imgPath in imagesPath:
        imagePath = imgPath
        # annotation file full path
        annotationName = imgPath.split(os.path.sep)[-1].replace('.jpg', '.xml')
        annotationPath = os.path.join(config.ANNOTATIONS_PATH, annotationName)
        # coopy images and annotations to corresponding file
        shutil.copy2(imagePath, path)
        shutil.copy2(annotationPath, path)
    except Exception as e:
      raise e

  def split(self):
    try:
      # garb the full path of all images
      imagesPath = [os.path.join(config.IMAGES_PATH, imageName) for imageName in os.listdir(config.IMAGES_PATH)]
      random.shuffle(imagesPath) 
      # split the images list into test and train
      limit = int(len(imagesPath) * config.SPLIT)
      
      trainset = imagesPath[:limit]
      testset = imagesPath[limit:]
      #build test and train dataset
      self.buildDataset(trainset, 'train')
      self.buildDataset(testset, 'test')
    except Exception as e:
      raise e

if __name__ == '__main__':
  spliter = DataSpliter()
  spliter.split()