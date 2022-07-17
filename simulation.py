"""
Общие идеи:
обучать предсказывалку будущего можно на нарезках из истории прошлого и чуть более поздних
последствий действий learn(t) = learn(t-2)*action(t-2) -> learn(t-1)

"""
from world import World, Agent
from brain import Brain
from base import Tickable
from model import Model

class Simulation(Tickable):
    """
    Главный класс, запускающий симуляцию. По идее, должен поддерживаться как одноагентный, так и
    многоагентный мир
    """
    # TODO: 1 экземляр симуляции работает в 1 процессе из multiprocessing
    def __init__(self, world, brains):
        self._world = world
        self._brains = brains
        for agent in self._world.agents:
            agent.link_brain(Brain(agent.inputs_count, agent.outputs_count, Model))

    def start(self):
        while True:
            self._world.tick()