import threading
from base import InputsOutputs

class Module(InputsOutputs):
    # TODO: модули должны работать в потоках
    def __init__(self):
        self.thread = threading.Thread(target=self.process)

    def process(self):
        pass


class Perception(Module):
    """
    Модуль восприятия должен сжимать входные данные и обрабатывать в понятную для модуля
    предсказания последовательность байт
    """
    pass


class Prediction(Module):
    """
     Модуль предсказания предсказывает результаты тех или иных действий(/бездействия) агента
    """
    pass


class Motivation(Module):
    """
    Модуль мотивации дает оценку текущей и будущей ситуации и оценивает полезность тех
    или иных действий для будущего с точки зрения расхода энергии в краткосроке и долгосроке
    """
    pass