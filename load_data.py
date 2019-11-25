"""
Loading data and test example

Usage:
> <python executable> - <the path to this file> - <path to the dataset> - <batch size>
OR
> <python executable> - <the path to this file> - <path to the dataset> (no generator is used)
Example:
> C:/Users/DIK/PycharmProjects/FER_project/venv/Scripts/python.exe
C:/Users/DIK/PycharmProjects/FER_project/load_data.py F:/dataset 3

Used Python 3.7.5

Requirements. Run these commands:
pip install Pillow
pip install numpy

Supported formats:
https://github.com/python-pillow/Pillow/blob/master/docs/handbook/image-file-formats.rst
"""

import os
import sys
import numpy
from PIL import Image

if len(sys.argv) == 1:  # the first argument is the script name itself
    raise Exception("Directory argument is missing")


class DataGenerator(object):
    def __init__(self, path):
        """
        Generator class that contains a method that yields the images and their labels from the specified path
        :param path: The path to the dataset: ex. "F:/dataset", containing uniquely named folders with the images
        """
        self.__path = path

    def __paths_generator(self):
        paths = []
        for root, dirs, files in os.walk(self.__path):
            for f in files:
                # validate here the file extension
                image_path = os.path.join(root, f)
                paths.append(image_path)
                yield image_path

    def __return_paths(self):
        paths = []
        for root, dirs, files in os.walk(self.__path):
            for f in files:
                # validate here the file extension
                image_path = os.path.join(root, f)
                paths.append(image_path)
        return paths

    def get_images(self):
        data = []
        labels = []
        image_paths = self.__return_paths()
        if not image_paths:
            raise Exception("No images were found")
        for path in image_paths:
            image = Image.open(path)
            numpy_array = numpy.asarray(image)
            data.append(numpy_array)
            label = path.split(os.path.sep)[-2]
            labels.append(label)
        return zip(data, labels)

    def data_generator(self, batch_size):
        start = 0
        paths_gen = self.__paths_generator()
        data = []
        labels = []
        while True:
            try:
                for i in range(0, batch_size):
                    path = next(paths_gen)
                    image = Image.open(path)
                    numpy_array = numpy.asarray(image)
                    data.append(numpy_array)
                    label = path.split(os.path.sep)[-2]
                    labels.append(label)

                yield data, labels
                start += batch_size
                data.clear()
                labels.clear()
            except StopIteration:
                yield data, labels  # get the last remaining elements and stop looping
                break


if __name__ == "__main__":
    batch_sz = int(sys.argv[2]) if len(sys.argv) == 3 else 0
    gen = DataGenerator(sys.argv[1])
    data = gen.data_generator(batch_sz) if batch_sz else gen.get_images()
    for _, y in data:
        print(y)
