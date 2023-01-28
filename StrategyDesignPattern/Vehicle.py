from Strategy.IDriveStrategy import IDriveStrategy
class Vehicle:

    def __init__(self, driveStrategy:IDriveStrategy) -> None:
        self.drive_strategy = driveStrategy
    
    def drive(self):
        self.drive_strategy.drive()
