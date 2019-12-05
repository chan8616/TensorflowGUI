from collections import OrderedDict
from gooey import Gooey, GooeyParser

from .model import Model
from model.keras_applications import run as runlib
from .config_samples import (InceptionV3TrainConfig,
                             InceptionV3TestConfig,
                             InceptionV3ImagenetConfig,
                             InceptionV3OlivettiFacesConfig,
                             InceptionV3CIFAR10Config)


def run_parser(
        parser: GooeyParser = GooeyParser(),
        title="Train Setting",
        ) -> GooeyParser:

    return runlib.run_parser(parser,
                             title,
                             train_config=InceptionV3TrainConfig(),
                             test_config=InceptionV3TestConfig(),
                             train_configs=OrderedDict([
                                 ('train_olivetti_faces', InceptionV3OlivettiFacesConfig()),
                                 ('train_cifar10', InceptionV3CIFAR10Config()),
                                 #  ('train_imagenet', InceptionV3ImagenetConfig()),
                             ]))


def run(config):
    return runlib.run(Model(), config, InceptionV3TrainConfig())
