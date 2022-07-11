from base import Tickable

class World(Tickable):
    """
    Интерфейс окружающей среды (мира для агента). Мир должен работать параллельно агенту, по идее
    И если агент зависнет, то он сдохнет, значит у него должны сформироваться такие механизмы,
    чтобы он не сдох
    Мир задаёт тело, в которое будет помещен мозг. Соответственно, количество входов и выходов агента определяется миром
    """
    # TODO: мир работает в потоке из threading, агент тоже
    def __init__(self, world):
        self._world = world
        # TODO: подумать, что из себя представляет мир в виде данных
        pass

class Agent:
    """
    Базовый тип для агентов любого мира. На основе него создаются "тела" для мозга, который ничего не должен знать о мире
    """
    def __init__(self, inputs_count, outputs_count, Brain_cls):
        self._inputs_count = inputs_count
        self._outputs_count = outputs_count
        self._brain = Brain_cls(inputs_count, outputs_count)

    @property
    def inputs_count(self):
        return self._inputs_count

    @property
    def outputs_count(self):
        return self._outputs_count