from module import Perception, Prediction, Motivation

class Model:
    """
    Модель содержит в себе конфигурацию из модулей (их соединение) и управляется мозгом извне
    Последний слой абстакции "[симуляция -> мир -> агент -> мозг -> модель]", который работает в основном потоке
    """
    def __init__(self, perception, prediction, motivation):
        self.configuration = []
        self._inputs = []
        self._outputs = []

    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        self._inputs = inputs

    @property
    def outputs(self):
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        self._outputs = outputs