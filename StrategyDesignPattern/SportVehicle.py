from Vehicle import Vehicle
from Strategy.SportDriveStrategy import SportDriveStrategy
class SportsVehicle(Vehicle):

    def __init__(self) -> None:
        super().__init__(SportDriveStrategy())