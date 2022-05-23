from agent import Agent
from world import World
from simulation import Simulation
from module import Perception, Prediction, Motivation

if __name__ == '__main__':
    """
    Базовый алгоритм: запуск симуляции, в идеале на время, пока агент не умрёт.
    В итоге должна посчитаться полезность агента с точки зрения выживания
    """
    simulation = Simulation(World, Agent)
    simulation.start()
