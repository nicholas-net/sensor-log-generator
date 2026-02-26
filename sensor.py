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

def save_readings_to_json(self, file_name):

    with open(file_name, "w") as f:
        json.dumps(file_name)

if __name__ == "__main__":

    # Generate the dataset
    sensor = WaterSensor(1)
    readings = []

    for i in range(97):
        readings.append(sensor.get_reading())

    readings.append(sensor.get_leak_reading())
    readings.append(sensor.get_blockage_reading())
    readings.append(sensor.get_stuck_reading())

    # Shuffle to mix anomalies
    random.shuffle(readings)

    print(f"Generated {len(readings)} readings!")
    print(f"First reading: {readings[0]}")
    print(f"Last reading: {readings[-1]}")


    # Save to JSON

    sensor_file = "sensor_data.json"
    save_readings_to_json(sensor_file)












