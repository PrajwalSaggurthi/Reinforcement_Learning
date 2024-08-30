import json

class RienforcementModel:
    def __init__(self):
        self.mapping = {
            'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10
        }
        self.learning_rate = 0.1

    def convert(self, text):
        return self.mapping.get(text, 0)

    def train(self, text, target):
        current = self.convert(text)
        error = target - current
        self.mapping[text] += self.learning_rate * error

    def reward(self, text):
        self.train(text, self.convert(text) + 0.1)

    def punish(self, text):
        self.train(text, self.convert(text) - 0.1)

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.mapping, f)

    def load(self, filename):
        with open(filename, 'r') as f:
            self.mapping = json.load(f)

