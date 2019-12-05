from pathlib import Path
import shutil

from keras.preprocessing.image import ImageDataGenerator  # type: ignore

from .. import dataset
from .directory_dataset_config import (
        DirectoryDatasetConfig,
        )

#  from ..dataset_samples.cifar10 import CIFAR10 as CIFAR10sample


class DIR_CIFAR10(dataset.CIFAR10,
                  DirectoryDatasetConfig):
    def __init__(self):
        super(DIR_CIFAR10, self).__init__()
        self.VAL_DIRECTORY = self.TEST_DIRECTORY


class DIR_MNIST(dataset.MNIST,
                DirectoryDatasetConfig):
    def __init__(self):
        super(DIR_MNIST, self).__init__()
        self.VAL_DIRECTORY = self.TEST_DIRECTORY


"""
class DGC_CIFAR100(ICGC_CIFAR100,
                   DirectoryGeneratorConfig):
    NAME = 'CIFAR100'

    def __init__(self):
        super(DGC_CIFAR100, self).__init__()

    def auto_download(self):
        pass


class DGC_FashionMNIST(ICGC_FashionMNIST,
                       DirectoryGeneratorConfig):
    NAME = 'FashionMNIST'

    def __init__(self):
        super(DGC_FashionMNIST, self).__init__()

    def auto_download(self):
        pass
"""

class DIR_OlivettiFaces(dataset.OlivettFaces,
                        DirectoryDatasetConfig):
    def __init__(self):
        super(DIR_OlivettiFaces, self).__init__()