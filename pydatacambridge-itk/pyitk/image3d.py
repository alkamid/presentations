import subprocess
from tempfile import TemporaryDirectory
from pathlib import Path

import SimpleITK as sitk
import itk
import numpy as np


class Image3D:
    def __init__(self, filename: str):
        self.img = self.read_image(filename)

    def read_image(self, filename):
        raise NotImplementedError

    def __getattr__(self, attr):
        return getattr(self.img, attr)


class ImageITK(Image3D):
    def __init__(self, filename: str):
        super().__init__(filename)

    def read_image(self, filename):
        return itk.imread(filename)
        

class ImageSITK(Image3D):
    def __init__(self, filename: str):
        super().__init__(filename)

    def read_image(self, filename):
        return sitk.ReadImage(filename)


class ImageNumpy(Image3D):
    def __init__(self, filename: str):
        super().__init__(filename)

    def read_image(self, filename):
        temp_img = itk.imread(filename)
        return itk.array_from_image(temp_img)


def itkindex(x, y, z):
    dimension = 3
    index = itk.Index[dimension]()
    index[0] = x
    index[1] = y
    index[2] = z
    return index