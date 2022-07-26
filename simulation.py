from world import World, Agent
from brain import Brain
from base import Tickable
from model import Model

class Simulation(Tickable):
    """
    Главный класс, запускающий симуляцию. По идее, должен поддерживаться как одноагентный, так и
    многоагентный мир
    Количество агентов задаётся настройками мира, симуляция ими не управляет. Однако, симуляция должна
    гарантировать присвоение мозга при создании в мире агента. Тогда мир должен иметь ссылку на симуляцию и возможность
    запросить очередной мозг для агента.
    """

    # TODO: 1 экземляр симуляции работает в 1 процессе из multiprocessing
    def __init__(self, world, brain_cls_list):
        self._world = world
        self._brains = brain_cls_list
        self._best_agent = None # Ссылка на лучшего по очкам приспособленности агента
        # Когда агент умирает, считаются его очки приспособленности. Они могут считаться и в другое время

    def start(self):
        while len(self._world._agents) > 0: # симуляция работает до последнего живого агента
            self._world.tick()
