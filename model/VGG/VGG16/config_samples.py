import os

from model.keras_applications.train_config import (
        WEIGHTS, LOSSES, OPTIMIZERS)
from generator.image_classification.config_samples \
        import (DIR_GEN_CIFAR10,
                DIR_GEN_OlivettiFaces,
                COLOR_MODES,
                )
from .train_config import VGG16TrainConfig
from .build_config import VGG16Config, POOLINGS


"""
class VGG16ImagenetConfig(
        VGG16Config, VGG16TrainConfig):
    NAME = os.path.join(VGG16Config.NAME, 'imagenet')
    CLASSES = 1000

    LOSS = LOSSES[2]
"""


class VGG16CIFAR10Config(
        VGG16Config,
        VGG16TrainConfig,
        DIR_GEN_CIFAR10,
        ):
    NAME = os.path.join(VGG16Config.NAME, DIR_GEN_CIFAR10.NAME)

    INPUT_SHAPE = (64, 64, 3)  # type: ignore

    POOLINGS = POOLINGS[0]
    HIDDEN_LAYERS = [64, 64]

    WEIGHT = WEIGHTS[0]  # type: ignore
    EPOCHS = 20
    #  VALIDATION_STEPS = 10

    LOSS = LOSSES[2]

    OPTIMIZER = OPTIMIZERS[1]
    LEARNING_RATE = 1e-4
    LEARNING_MOMENTUM = 0.0

    def __init__(self):
        super(VGG16CIFAR10Config, self).__init__()
        self.CLASSES = len(self.LABELS)
        self.TARGET_SIZE = self.INPUT_SHAPE[:2]


class VGG16OlivettiFacesConfig(
        VGG16Config,
        VGG16TrainConfig,
        DIR_GEN_OlivettiFaces,
        ):
    NAME = os.path.join(VGG16Config.NAME, DIR_GEN_OlivettiFaces.NAME)

    INPUT_SHAPE = (64, 64, 3)  # type: ignore

    POOLINGS = POOLINGS[0]
    HIDDEN_LAYERS = [256, 256]

    WEIGHT = WEIGHTS[0]  # type: ignore
    EPOCHS = 20
    #  VALIDATION_STEPS = 10

    LOSS = LOSSES[2]

    OPTIMIZER = OPTIMIZERS[1]
    LEARNING_RATE = 1e-4
    LEARNING_MOMENTUM = 0.0

    def __init__(self):
        super(VGG16OlivettiFacesConfig, self).__init__()
        self.CLASSES = len(self.LABELS)
        self.TARGET_SIZE = self.INPUT_SHAPE[:2]
        self.COLOR_MODE = COLOR_MODES[1]