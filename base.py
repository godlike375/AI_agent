class Tickable:
    def tick(self):
        pass

class InputsOutputs:
    def __init__(self):
        self._inputs = []
        self._outputs = []

    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        self._inputs = inputs

    #выходы нельзя изменять извне, только изнутри
    @property
    def outputs(self):
        return self._outputs