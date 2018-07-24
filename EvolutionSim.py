from Population import Population
import FlapPyBird.flappy as emulator


class EvoSim(object):
    def __init__(self, pop_size=10, mutation_rate=0.05, mutation_scale = 0.3, generations=10):
        self.pop_size = pop_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.mutation_scale = mutation_scale
        self.pop = Population(pop_size, mutation_rate, mutation_scale)
        self.emulator = emulator.Emulator()

    def simulate(self):
        for i in range(self.generations):
            self.pop.calculate_current_gen(self.emulator)
            self.pop.generate_next_generation()

        # TODO play indefinitely the best player
