from module import Perception, Prediction, Motivation
from base import Tickable, InputsOutputs

class Model(Tickable, InputsOutputs):
    """
    Модель содержит в себе конфигурацию из модулей (их соединение) и управляется мозгом извне
    Последний слой абстакции "[симуляция -> мир -> агент -> мозг -> модель]", который работает в основном потоке
    """
    def __init__(self, perception, prediction, motivation):
        self.configuration = []
