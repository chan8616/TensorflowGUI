import datetime
from pathlib import Path
from gooey import Gooey, GooeyParser

from .model import KerasAppBaseModel
from .build import build
from .train import TrainConfig, train_config_parser, train  # , train_config
from .test import TestConfig, test_config_parser, test
from .generator import generator

from keras import backend as K

#  from . import (train_config,
#                 build,
#                 build_config,
#                 train,
#                 config
#                 test, test_config,
#                 generator, generator_config,
#                 )


def run_parser(
        parser: GooeyParser = GooeyParser(),
        title="Run Setting",
        train_config=TrainConfig(),
        train_configs={},
        test_config=TestConfig(),
        test_configs={},
        ) -> GooeyParser:

    subs = parser.add_subparsers()

    test_parser = subs.add_parser('test')
    test_config_parser(test_parser, test_config=test_config)

    for k, v in train_configs.items():
        train_parser = subs.add_parser(k)
        train_config_parser(train_parser, train_config=v)

    train_parser = subs.add_parser('train')
    train_config_parser(train_parser, train_config=train_config)

    return parser


# Should be fixed. It is directly used in gui/frame.py
def run(model: KerasAppBaseModel, config):
    print(config)
    (build_cmds, build_args,
     run_cmds, run_args,
     generator_cmds, generator_args,
     stream) = config
    run_cmd = run_cmds[0]

    #  model = build.build(build_args)
    #  model.build(build_args)
    print('before build')
    build(model, build_args)

    print('before load')
    if run_args.load_pretrained_weights:
        if run_args.load_pretrained_weights == "imagenet":
            # Start from ImageNet trained weights
            weights_path = model.get_imagenet_weights()
        elif run_args.load_pretrained_weights == "last":
            # Find last trained weights
            weights_path = model.find_last()
        else:
            weights_path = run_args.load_pretrained_weights

        model.load_weights(weights_path, by_name=True)
    print('load complete')

    print('before generator')
    generator_cmd = generator_cmds[0]

    train_generator, val_generator = generator(generator_cmd, generator_args)
    print('generator complete')

    if 'train' in run_cmd:
        print('before train')
        train_args = run_args
        #  model.train(train_args, train_generator, val_generator)
        train(model, train_args, train_generator, val_generator, stream)
        print('train complete')
    elif 'test' == run_cmd:
        print('before test')
        test_args = run_args
        test_generator = val_generator

        test(model, test_args, test_generator)
        print('test complete')
    K.clear_session()
