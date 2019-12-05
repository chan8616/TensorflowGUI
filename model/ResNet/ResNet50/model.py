from pathlib import Path
from keras.utils.data_utils import get_file  # type: ignore
from keras.applications.resnet50 import ResNet50  # type: ignore

from model.model_config import ModelConfig
from model.keras_applications import model as modellib

TF_WEIGHTS_PATH_NO_TOP = (
        'https://github.com/fchollet/deep-learning-models/releases/download/'
        'v0.2/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5')


class Model(modellib.KerasAppBaseModel):
    def __init__(self, model_config=ModelConfig()):
        super(Model, self).__init__(ResNet50, model_config)

    def get_imagenet_weights(self):
        """Downloads ImageNet trained weights from Keras.
        Returns path to weights file.
        """
        weights_path = get_file(str(Path(TF_WEIGHTS_PATH_NO_TOP).name),
                                TF_WEIGHTS_PATH_NO_TOP,
                                cache_subdir='models',
                                file_hash='a268eb855778b3df3c7506639542a6af')
        return weights_path

    def set_trainable(self, layers):
        for layer in self.keras_model.layers[
                :layers]:
            layer.trainable = False
        for layer in self.keras_model.layers[
                layers:]:
            layer.trainable = True