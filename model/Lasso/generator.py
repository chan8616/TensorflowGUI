from argparse import Namespace
from pathlib import Path
from typing import Union
from gooey import Gooey, GooeyParser

import pandas as pd
from sklearn.preprocessing import StandardScaler

from .generator_config import LassoGeneratorConfig
from model.Lasso.config_samples import LassoBostonHousePricesConfig


class LassoGeneratorConfigList():
    def __init__(self,
                 Lasso_generator_config_list=[
                     LassoBostonHousePricesConfig(),
                     LassoGeneratorConfig(),
                     ],
                 ):
       self.Lasso_generator_config_list = Lasso_generator_config_list

    def config(self, cmd, args):
        for config in self.Lasso_generator_config_list:
            if config.NAME == cmd:
                config.update(args)
                return config

    def _sub_parser(self, subs=GooeyParser().add_subparsers()):
        for config in self.Lasso_generator_config_list:
            parser = subs.add_parser(config.NAME)
            config._parser(parser)

    def _parser(self, parser=GooeyParser()):
        subs = parser.add_subparsers()
        self._sub_parser(subs)
        return parser


generator_parser = LassoGeneratorConfigList()._parser


class LassoGenerator():
    def __init__(self, Lasso_generator_config=LassoGeneratorConfig()):
        self.config = Lasso_generator_config

    def train_valid_generator(self):
        try:
            dataframe = pd.read_csv(self.config.DATAFRAME_PATH)

            standard_scaler = StandardScaler()
            standard_scaler.fit(dataframe[self.config.X_COL])
            dataframe[self.config.X_COL] = \
                standard_scaler.transform(dataframe[self.config.X_COL])
        except Exception as e:
            print(e)
            assert False, "wrong dataframe path {}.".format(
                    self.config.DATAFRAME_PATH)
        train_data = dataframe[self.config.X_COL], dataframe[self.config.Y_COL]

        if self.config.VALID_DATAFRAME_PATH:
            try:
                valid_dataframe = pd.read_csv(self.config.VALID_DATAFRAME_PATH)
                valid_dataframe[self.config.X_COL] = \
                    standard_scaler.transform(valid_dataframe[self.config.X_COL])
            except Exception as e:
                print(e)
                assert False, "wrong dataframe path {}.".format(
                    self.config.VALID_DATAFRAME_PATH)
            valid_data = valid_dataframe[self.config.X_COL], valid_dataframe[self.config.Y_COL]
        else:
            valid_data = None
        return (train_data, valid_data)
