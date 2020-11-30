# Credits: TensorFlow Object Detection API team
# https://github.com/tensorflow/models/tree/master/research/object_detection
# we will intoduce a small modification. 
import os
import pandas as pd
import glob
import xml.etree.ElementTree as ET

def xml_to_csv (path):
  try:
    xml_list = list()
    for xml_file in glob.glob(path + '/*.xml'):
      three = ET.parse(xml_file)
      root = three.getroot()
      for member in root.findall('object'):
        filename = root.find('filename').text
        if ' (' in filename:
          filename = filename.replace(' (', '_').replace(')', '')+'.jpg'

        value=(
          filename,
          int(root.find('size')[0].text),
          int(root.find('size')[1].text),
          member[0].text,
          int(member[4][0].text),
          int(member[4][1].text),
          int(member[4][2].text),
          int(member[4][3].text)
        )
        xml_list.append(value)

    column_name = ['filename' , 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    df = pd.DataFrame(xml_list, columns=column_name)
    return df

  except Exception as e:
    raise e

def main ():
  try:
    for directory in ['train', 'test']:
      imagePath = os.path.join(os.getcwd(), 'dataset', directory)
      df = xml_to_csv(imagePath)
      csvPath = directory +'_labels.csv'
      df.to_csv(csvPath, index=None)
  except Exception as e:
    raise e
    
#main()
