"""
Общие идеи:
обучать предсказывалку будущего можно на нарезках из истории прошлого и чуть более поздних
последствий действий learn(t) = learn(t-2)*action(t-2) -> learn(t-1)

"""


class Simulation:
    """
    Главный класс, запускающий симуляцию. По идее, должен поддерживаться как одноагентный, так и
    многоагентный мир
    """
    # TODO: 1 экземляр симуляции работает в 1 процессе из multiprocessing
    def __init__(self, world_cls, agent_cls):
        self._environment = world_cls()
        self._agent = agent_cls()

    def start(self):
        pass