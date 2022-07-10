import threading

class Module:
    # TODO: модули должны работать в потоках
    def __init__(self):
        self._inputs = []
        self._outputs = []
        self.thread = threading.Thread(target=self.process)

    def process(self):
        pass

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