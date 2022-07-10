class Brain:
    """
    Мозг может только принимать данные через get_inputs, обрабатывать и
    и выставлять на абстрактные "мышцы" сигналы через set_outputs
    Всё остальное, в том числе "тело" агента является частью "мира" и обработкой действий агента
    занимается класс Simulation, то есть действие, которое делает агент своими выходами,
    становится таковы действием именно в рамках внешнего мира, но не самого агента
    Мозг по факту является только функцией преобразования входов в выходы
    """
    # TODO: мир работает в потоке из threading, агент тоже
    def __init__(self, inputs_count, outputs_count, Model):
        # TODO: сделать интерфейс "тело" для обмена информацией с внешним миром (потоком симуляции)
        # возможно модули могут состоять из подмодулей (что логично), у агента должен быть просто
        # список модулей с порядком пропускания информациии через них или связями между ними (как модель в Tensorflow)
        self._model = Model(inputs_count, outputs_count)
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

    def start(self):
        while True:
            self._model.inputs = self.inputs
            self._model.outputs = self.outputs

