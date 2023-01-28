from Strategy.IDriveStrategy import IDriveStrategy

class NormalDriveStrategy(IDriveStrategy):
    def drive(self):
        print('I drive normally')