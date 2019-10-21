from typing import Union
from argparse import ArgumentParser, _ArgumentGroup
from gooey import Gooey, GooeyParser

from keras.optimizers import sgd, SGD, adam, Adam


def get_optimizer_parser(
        parser: Union[ArgumentParser, GooeyParser,
                      _ArgumentGroup] = GooeyParser(),
        title="Optimizer Setting",
        description=""):
    assert isinstance(parser,
                      (ArgumentParser, GooeyParser, _ArgumentGroup)
                      ), type(parser)

    if isinstance(parser, (ArgumentParser, GooeyParser)):
        optimizer_parser = parser.add_argument_group(
            title=title,
            description=description,
            gooey_options={'columns': 3}
        )
    elif isinstance(parser, _ArgumentGroup):
        optimizer_parser = parser
    else:
        raise ValueError

    optimizer_parser.add_argument(
        "--optimizer", choices=["sgd", "adam", "rmsprop"],
        default="sgd",
    )
#    optimizer_optimizer_parseradd_argument(
    optimizer_parser.add_argument(
        "--learning_rate", type=float, default=.001,
    )

    def get_optimizer(args):
        if args.optimizer == 'sgd':
            return sgd(args.learning_rate)
        if args.optimizer == 'SGD':
            return SGD(args.learning_rate)
        if args.optimizer == 'adam':
            return adam(args.learning_rate)
        if args.optimizer == 'Adam':
            return Adam(args.learning_rate)
        raise NotImplementedError

    parser.set_defaults(get_optimizer=get_optimizer)

    return parser


if __name__ == "__main__":
    parser = GooeyParser()
    Gooey(get_optimizer_parser)(
        parser.add_argument_group()
    )
    args = parser.parse_args()
    print(args)