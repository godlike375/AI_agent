from simulation import Simulation

"""
Метавселенная - множество запущенных симуляций с возможно разными мирами
с целью подбора наиболее оптимальных гиперпараметров мозга для выживания в любом возможном мире
А ля параллельные реальности, которые отличаются действиями агентов из-за разных мозгов
"""

class Metaverse():

    def __init__(self, brain_cls_list, world_cls):
        world = world_cls()
        self._simulations = [Simulation(world, brain_cls_list)]

    def run(self):
        for simulation in self._simulations:
            simulation.start()
