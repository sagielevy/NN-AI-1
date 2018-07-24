import keras
from Population import Population
import FlapPyBird.flappy as emulator


class EvoSim(object):
    def __init__(self, pop_size=10, mutation_rate=0.05, mutation_scale = 0.3, generations=10):
        self.pop = Population(pop_size, mutation_rate, mutation_scale)
        self.emulator = emulator.Emulator()

    def simulate(self):
        pass
