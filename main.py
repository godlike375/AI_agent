from brain import Brain
from world import World
from simulation import Simulation
from metaverse import Metaverse

if __name__ == '__main__':
    """
    Базовый алгоритм: запуск симуляции, в идеале на время, пока агент не умрёт или не выполнит цель симуляции.
    В итоге должна посчитаться полезность агента с точки зрения выживания
    """

    brain_cls_list = [] # TODO: как получить список классов мозгов?
    world_cls = World
    metaverse = Metaverse(brain_cls_list, world_cls)
    best_brain_config = metaverse.run()
