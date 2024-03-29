from simulation import Simulation

"""
Метавселенная - множество запущенных симуляций с возможно разными мирами
с целью подбора наиболее оптимальных гиперпараметров мозга для выживания в любом возможном мире
А ля параллельные реальности, которые отличаются действиями агентов из-за разных мозгов
Либо разные мозги в одном мире, либо
разные миры с одним мозгом
как поддержать разные миры с разными
мозгами?
Разные миры могут быть как по классу, так
и по состоянию
!Разные мозги в одном мире должны симулироваться с одинаковых стартовых условий, чтобы всё было честно
"""

class Metaverse():

    def __init__(self, brains_list, worlds_list):
      if len(brains_list) > 1:
        assert len(worlds_list) == 1
        # симулируем много мозгов в одном типе мира
      elif len(brains_list) == 1:
        assert len(worlds_list) > 1
        # симулируем много миров с одним мозгом
        self._simulations = [Simulation(world, brain_cls_list)]

    def run(self):
        for simulation in self._simulations:
            simulation.start()
