import random
import json
import datetime as dt
from datetime import timezone
from itertools import count


class WaterSensor:
    """
        Simulates a Hydroficient HYDROLOGIC water sensor.

        Normal ranges:
        - pressure_upstream: 75-90 PSI
        - pressure_downstream: 70-85 PSI
        - flow_rate: 30-50 gallons/min
    """
    def __init__(self, device_id: int):
        self.device_id = device_id
        self.counter = 0
        self.base_pressure_upstream = 82.5
        self.base_pressure_downstream = 77.5
        self.base_flow_rate = 40

    def __generate_reading(self):
        self.counter += 1
        time_stamp = dt.datetime.now(dt.timezone.utc).isoformat()
        pressure_upstream = round(random.uniform(self.base_pressure_upstream, 90.0), 1)
        pressure_downstream = round(random.uniform(self.base_pressure_downstream, 85.0), 1)
        flow_rate = round(random.uniform(self.base_flow_rate, 50.0), 1)

        return {
            "device_id": f"GM-HYDROLOGIC-{self.device_id}",
            "timestamp": time_stamp,
            "counter": self.counter,
            "pressure_upstream": pressure_upstream,
            "pressure_downstream": pressure_downstream,
            "flow_rate": flow_rate
        }


    def get_reading(self):
        """
        Generate a normal sensor reading.
        - Increment the counter
        - Create timestamp in ISO 8601 UTC format
        - Generate realistic pressure and flow values with small variation
        - Return a dictionary with all fields
        """
        return self.__generate_base_reading()

        # def get_leak_reading(self):
        #
        #     leak_flow_rate = round(random.uniform(80.0,120.0))


    #def get_blockage_reading(self):
    # TO DO
    #def get_stuck_reading(self):

water_sensor_1 = WaterSensor(1)
water_sensor_2 = WaterSensor(2)
print(water_sensor_1.get_reading())
print(water_sensor_1.get_reading())
#print(water_sensor_1.get_leak_reading())




