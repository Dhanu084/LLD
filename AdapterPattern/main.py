from WeightInPounds.BabyWeighingMachine import BabyWeighingMachine
from Adapter.WeightInKg import WeightInKg

if __name__=="__main__":
    babyweighingmachine = BabyWeighingMachine()
    print(WeightInKg(babyweighingmachine).weight())
