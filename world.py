import threading
from base import Tickable


class World(Tickable):
    """
    Интерфейс окружающей среды (мира для агента). Мир должен работать параллельно агенту, по идее
    И если агент зависнет, то он сдохнет, значит у него должны сформироваться такие механизмы,
    чтобы он не сдох
    Мир задаёт тело, в которое будет помещен мозг. Соответственно, количество входов и выходов агента определяется миром
    """
    # TODO: мир работает в потоке из threading, агенты и объекты обрабатываются в этом же потоке
    def __init__(self):
        self.agents = []
        self.objects = []
        # TODO: подумать, что из себя представляет мир в виде данных
        pass

    def request_brain(self, agent):
        # запрос к симуляции выдать агенту мозг
        new_brain = # TODO: решить, откуда брать мозг
        agent._brain = new_brain
        pass

    def score_agent(self, agent):
        # Получить очки приспособленности агента, на основе которых симуляция будет решать об интеллектуальности
        # того или иного мозга
        pass

    def tick(self):
        for agent in self._agents:
            agent.tick()
        for object in self._objects:
            object.tick()


class Agent(Tickable):
    """
    Базовый тип для агентов любого мира. На основе него создаются "тела" для мозга, который ничего не должен знать о мире
    """
    def __init__(self, inputs_count, outputs_count, world):
        self._inputs_count = inputs_count
        self._outputs_count = outputs_count
        self._world = world

    def link_brain(self, brain):
        self._brain = brain

    @property
    def inputs_count(self):
        return self._inputs_count

    @property
    def outputs_count(self):
        return self._outputs_count

    def tick(self):
        self._brain.inputs = self.get_inputs()
        self.act(self.decode(self._brain.outputs))

    def decode(self, outputs):
        # Здесь должна быть расшифровка сигналов от мозга
        pass

    def act(self, decoded):
        # Здесь выбор действий с миром в зависимости от расшифрованных сигналов
        pass


class Object(Tickable):
    """
    Базовый тип для объектов мира. Объект - набор свойств (полей)
    """
    def __init__(self, type, props):
        self.type = type
        self.properties = props or {}  # мб обычный лист

    def tick(self):
        pass