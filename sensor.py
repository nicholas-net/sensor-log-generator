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
        time_stamp = dt.datetime.now(timezone.utc).isoformat()
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
        return self.__generate_reading()

    def get_leak_reading(self) -> dict:

        leak_reading = self.__generate_reading()
        leak_flow_rate = round(random.uniform(80.0,120.0), 1)
        leak_reading["flow_rate"] = leak_flow_rate

        return leak_reading

    def get_blockage_reading(self) -> dict:

        blockage_reading = self.__generate_reading()
        blockage_reading["pressure_upstream"] = round(random.uniform(95.0,110.0), 1)
        blockage_reading["pressure_downstream"] = round(random.uniform(50.0, 65.0), 1)

        return blockage_reading

    def get_stuck_reading(self) -> dict:

        stuck_reading = self.__generate_reading()
        stuck_reading["pressure_downstream"] = stuck_reading["pressure_upstream"]
        stuck_reading["flow_rate"] = stuck_reading["pressure_downstream"]

        return stuck_reading



if __name__ == "__main__":

    # Test Sensor
    sensor = WaterSensor(1)

    print("=== Testing Normal Readings ===")
    for i in range(5):
        reading = sensor.get_reading()
        print(f"Reading {i+1}: Counter={reading['counter']}, "
              f"Pressure Up={reading['pressure_upstream']}, "
              f"Flow={reading['flow_rate']}")

        print("\n=== Testing Anomalies ===")
        print(f"Leak: {sensor.get_leak_reading()}")
        print(f"Blockage: {sensor.get_blockage_reading()}")
        print(f"Stuck: {sensor.get_stuck_reading()}")






