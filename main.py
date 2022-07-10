from brain import Brain
from world import World
from simulation import Simulation

if __name__ == '__main__':
    """
    Базовый алгоритм: запуск симуляции, в идеале на время, пока агент не умрёт или не выполнит цель симуляции.
    В итоге должна посчитаться полезность агента с точки зрения выживания
    """
    simulation = Simulation(World, Brain)
    simulation.start()
