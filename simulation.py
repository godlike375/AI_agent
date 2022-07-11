"""
Общие идеи:
обучать предсказывалку будущего можно на нарезках из истории прошлого и чуть более поздних
последствий действий learn(t) = learn(t-2)*action(t-2) -> learn(t-1)

"""
from world import World
from brain import Brain
from base import Tickable

class Simulation(Tickable):
    """
    Главный класс, запускающий симуляцию. По идее, должен поддерживаться как одноагентный, так и
    многоагентный мир
    """
    # TODO: 1 экземляр симуляции работает в 1 процессе из multiprocessing
    def __init__(self, world: World, brains: list[Brain]):
        self._world = world
        self._brains = brains

    def start(self):
        for brain in self._brains:
            brain.start()