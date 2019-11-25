from argparse import Namespace
from pathlib import Path
from typing import Union
from gooey import Gooey, GooeyParser

import model as modellib
from .model import KerasAppBaseModel
from .build_config import BuildConfig, build_config_parser


def build_parser(
        parser: GooeyParser = GooeyParser(),
        title="Build Setting",
        build_config=BuildConfig(),
        build_configs={},
        #  imagenet_config=BuildConfig(),
        ) -> GooeyParser:

    subs = parser.add_subparsers()

    for k, v in build_configs.items():
        build_parser = subs.add_parser(k)
        build_config_parser(build_parser, title, v)

    build_parser = subs.add_parser('build')
    build_config_parser(build_parser, title, build_config)

    #  base_build_parser = subs.add_parser('build_check')
    #  build_config_parser(base_build_parser, title, imagenet_config)

    #  build_parser = subs.add_parser('build')
    #  build_config_parser(build_parser, title, build_config)

    #  base_build_parser = subs.add_parser('build_imagenet')
    #  build_config_parser(base_build_parser, title, imagenet_config)

    return parser


def build(model: KerasAppBaseModel, build_args: Namespace) -> None:
    build_config = BuildConfig()
    build_config.update(build_args)
    model.build(build_config=build_config)
    print([layer.name for layer in model.keras_model.layers])

    if build_args.print_model_summary:
        print(model.keras_model.summary())
