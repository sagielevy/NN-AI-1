import keras
import os


class Agent(object):
    def __init__(self, agent_id, parents=None):
        self.agent_id = agent_id

        self.score = 0
        self.fitness = 0
        self.model = None

    def act(self, dif_x, dif_y, velocity_y):
        pass

    def update_score(self, score):
        pass

    def _gen_agent(self, parents, mutation_rate, mutation_scale):
        pass

    def _build_model(self):
        pass
