class Agent:
    # TODO: мир работает в потоке из threading, агент тоже
    def __init__(self, perception, prediction, motivation):
        # возможно модули могут состоять из подмодулей (что логично), у агента должен быть просто
        # список модулей с порядком пропускания информациии через них или связями между ними
        self.perception = perception
        self.prediction = prediction
        self.motivation = motivation

    def run(self):
        while True:
            self.perception.process()
            pass

    def get_inputs(self):
        return

