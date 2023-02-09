from Adapter.IWeightInKg import IWeightInKg


class WeightInKg(IWeightInKg):
    def __init__(self, weightInPounds) -> None:
        self.weightInPounds = weightInPounds
    def weight(self):
        return self.weightInPounds.weight() + self.weightInPounds.weight() * 0.5