from typing import Union, Callable
from argparse import ArgumentParser, _ArgumentGroup
from gooey import GooeyParser

from keras.callbacks import ModelCheckpoint, EarlyStopping
from model.utils.callbacks_ import MyCSVLogger


def get_callbacks_parser(
    parser: Union[ArgumentParser, GooeyParser] = GooeyParser(),
    title: str = "Callbacks Setting",
    # paths: {'ckpt_file_path': "checkpoint/model.h5"}
    # ckpt_file_path: str = "checkpoint/model.h5",
    model_dir: str = "checkpoint/"
) -> Callable:
    """"""
    checkpoint_parser = parser.add_argument_group(
        title=title,
        description="checkpoint callback",
        gooey_options={'columns': 3, 'show_border': True}
    )
    checkpoint_parser.add_argument(
        '--use-checkpoint-callback',
        action='store_true', default=False,
    )
    checkpoint_callback_parser(checkpoint_parser,
                               model_dir=model_dir)

    earlystopping_parser = parser.add_argument_group(
        title=None,
        description="earlystopping callback",
        gooey_options={'columns': 3, 'show_border': True}
    )
    earlystopping_parser.add_argument(
        '--use-earlystopping-callback',
        action='store_true', default=False,
    )
    earlystopping_callback_parser(earlystopping_parser)

    return parser


def get_callbacks(args):
    callbacks = []
    if args.use_checkpoint_callback:
        callbacks.append(
            get_checkpoint_callback(args))

    if args.use_earlystopping_callback:
        callbacks.append(
            get_earlystopping_callback(args))
    return callbacks


def checkpoint_callback_parser(
        parser: Union[ArgumentParser, GooeyParser,
                      _ArgumentGroup] = GooeyParser(),
        title: str = "Checkpoint Options",
        description: str = "",
        model_dir: str = "checkpoint/"
        ) -> Callable:

    if isinstance(parser, (ArgumentParser, GooeyParser)):
        checkpoint_parser = parser.add_argument_group(
            title=title,
            description=description,
            gooey_options={'columns': 3})
    elif isinstance(parser, _ArgumentGroup):
        checkpoint_parser = parser
    else:
        raise ValueError

    checkpoint_parser.add_argument(
        '--ckpt-file-path',
        default=model_dir+"trained_model.hd5",
        gooey_options={
            'validator': {
                'test': "user_input[:len('"+model_dir+"')]=='"+model_dir+"'",
                'message': 'unvalid save path'
            }
        })
    checkpoint_parser.add_argument(
        '--monitor',
        choices=['acc', 'loss', 'val_loss', 'val_acc'],
        default='loss')
    checkpoint_parser.add_argument('--save-best-only', action='store_true')
    checkpoint_parser.add_argument('--save-weights-only', action='store_true')
    checkpoint_parser.add_argument('--period', type=int, default=1)

    return parser


def get_checkpoint_callback(args):
    return ModelCheckpoint(
        args.ckpt_file_path,
        monitor=args.monitor,
        save_best_only=args.save_best_only,
        save_weights_only=args.save_weights_only,
        period=args.period
        )


def earlystopping_callback_parser(
        parser: Union[ArgumentParser, GooeyParser,
                      _ArgumentGroup] = GooeyParser(),
        title="EalyStopping Options",
        description="",
        ) -> Callable:

    if isinstance(parser, (ArgumentParser, GooeyParser)):
        earlystopping_parser = parser.add_argument_group(
            title=title,
            description=description,
            gooey_options={'columns': 3})
    elif isinstance(parser, _ArgumentGroup):
        earlystopping_parser = parser

    earlystopping_parser.add_argument('--min_delta')
    earlystopping_parser.add_argument('--patience')
    earlystopping_parser.add_argument('--baseline')
    earlystopping_parser.add_argument('--restore_best_weights')

    return parser


def get_earlystopping_callback(args):
    return EarlyStopping(
        monitor=args.monitor,
        min_delta=args.min_delta,
        patience=args.patience,
        baseline=args.baseline,
        restore_best_weights=args.restore_best_weights
        )


def csvlogger_callback_parser(
        parser: Union[ArgumentParser, GooeyParser,
                      _ArgumentGroup] = GooeyParser(),
        title="CSVLogger Options",
        description="",
        ) -> Callable:

    if isinstance(parser, (ArgumentParser, GooeyParser)):
        csvlogger_parser = parser.add_argument_group(
            title=title,
            description=description,
            gooey_options={'columns': 3})
    elif isinstance(parser, _ArgumentGroup):
        csvlogger_parser = parser

    csvlogger_parser.add_argument(
        '--filename', type=str)
    # csvlogger_parser.add_argument(
    #     '--separator', type=str, default=',')
    # csvlogger_parser.add_argument(
    #     '--append', action='store_true')


def get_csvlogger_callback(args):
    return MyCSVLogger(
        filename=args.filename,
        # separator=args.separator,
        # append=args.append
    )