
from ParkingLot.enums import VehicleType
from ParkingLot.entity import Vehicle, ParkingSpot
from ParkingLot.look_up_strategy import RandomLookUpStrategy
from ParkingLot.spot_managers import TwoWheelerSpotManager, FourWheelerSpotManager
from ParkingLot.parking_lot import ParkingLevel, ParkingBuilding, ParkingLot, EntranceGate, ExitGate
from ParkingLot.pricing import CostComputation, FixedPricingStrategy
from ParkingLot.payment import CashPayment, UPIPayment


def main():

    strategy =  RandomLookUpStrategy()
    level_one_managers = {
        VehicleType.TWO_WHEELER : TwoWheelerSpotManager(
            spots=[ParkingSpot("L1-S1"), ParkingSpot("L1-S2")], 
            strategy=strategy
        ),
        VehicleType.FOUR_WHEELER : FourWheelerSpotManager(
            spots=[ParkingSpot("L1-S3"), ParkingSpot("L1-S4")], 
            strategy=strategy
        )
    }

    level_1 = ParkingLevel(level_number = 1, managers = level_one_managers)

    level_two_managers = {
        VehicleType.TWO_WHEELER : TwoWheelerSpotManager(
            spots=[ParkingSpot("L2-S1"), ParkingSpot("L2-S2")], 
            strategy=strategy
        ),
        VehicleType.FOUR_WHEELER : FourWheelerSpotManager(
            spots=[ParkingSpot("L2-S3"), ParkingSpot("L2-S4")], 
            strategy=strategy
        )
    }

    level_2 = ParkingLevel(level_number = 2, managers = level_two_managers)

    pricing_strategy = CostComputation(FixedPricingStrategy())
    building = ParkingBuilding(levels=[level_1, level_2], cost_computation = pricing_strategy)

    parking_lot = ParkingLot(
        building = building, 
        entrace_gate = EntranceGate(),  
        exit_gate = ExitGate(cost_computation = pricing_strategy)
    )

    bike = Vehicle(vehicle_number = "BIKE-101", vehicle_type = VehicleType.TWO_WHEELER)
    car = Vehicle(vehicle_number = "CAR-201", vehicle_type = VehicleType.FOUR_WHEELER)

    print("--- Simulating Vehicles Arriving ---")
    b1 = parking_lot.vehicle_arrives(bike)
    b2 = parking_lot.vehicle_arrives(bike)
    b3 = parking_lot.vehicle_arrives(bike)
    b4 = parking_lot.vehicle_arrives(bike)
    c1 = parking_lot.vehicle_arrives(car)


    print("--- Simulating Vehicles Exiting ---")
    parking_lot.vehicle_exits(b1, CashPayment())
    parking_lot.vehicle_exits(c1, UPIPayment())
    

if __name__ == "__main__":
    main()