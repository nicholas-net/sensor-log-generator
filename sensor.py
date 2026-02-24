import random
import json
import datetime as dt
from datetime import timezone
from itertools import count


class WaterSensor:
    def __init__(self, device_id):
        self.device_id = device_id
        self.counter = 0
        self.base_pressure_upstream = 82.5
        self.base_pressure_downstream = 77.5
        self.base_flow_rate = 40

    def get_reading(self):
        self.counter+=1
        time_stamp = dt.datetime.now(dt.timezone.utc).isoformat()
        pressure_upstream = round(random.uniform(self.base_pressure_upstream, 90.0),1)
        pressure_downstream = round(random.uniform(self.base_pressure_downstream, 85.0),1)
        flow_rate = round(random.uniform(self.base_flow_rate,50.0),1)

        reading_info = {}

        return {
            "device_id": f"GM-HYDROLOGIC-{self.counter}",
            "timestamp": time_stamp,
            "counter": self.counter,
            "pressure_upstream": pressure_upstream,
            "pressure_downstream": pressure_downstream,
            "flow_rate": flow_rate
        }

water_sensor_1 = WaterSensor(1)
print(water_sensor_1.get_reading())




