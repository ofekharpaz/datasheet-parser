import re
from typing import Set, Tuple, Optional

class Component:
    def __init__(self, name: str):
        self.name: str = name
        self.voltage_range: Optional[Tuple[float, float]] = None
        self.temperature_range: Optional[Tuple[float, float]] = None

    def parse_ranges(self, text: str) -> None:
        """
        Given text, extract all occurnces of operating voltage range and operating temperature range.
        If there is more than 1 occurance of a range, set that range to None.
        Args:
            text (str): text describing the component.
        """
        voltage_pattern: str = r"(-?\d+(\.\d+)?)\s*V\s*to\s*(-?\d+(\.\d+)?)\s*V"
        temperature_pattern: str = r"([-+]?\d+(\.\d+)?)\s*°?\s*C\s*to\s*([-+]?\d+(\.\d+)?)\s*°?\s*C"

        voltage_ranges: Set[Tuple[float, float]] = self.extract_ranges(text, voltage_pattern)
        temperature_ranges: Set[Tuple[float, float]] = self.extract_ranges(text, temperature_pattern)

        self.set_range(voltage_ranges, temperature_ranges)

    def extract_ranges(self, text: str, pattern: str) -> Set[Tuple[float, float]]:
        """
        Given text and a regular expression pattern, returns a set of tuples that contains the ranges
        """
        ranges: Set[Tuple[float, float]] = set()
        matches = re.finditer(pattern, text)
        for match in matches:
            if match.group(1) is not None and match.group(3) is not None:
                ranges.add((float(match.group(1)), float(match.group(3))))
        return ranges

    def set_range(self, voltage_ranges: Set[Tuple[float, float]], temperature_ranges: Set[Tuple[float, float]]) -> None:
        if len(voltage_ranges) == 1:
            self.voltage_range = voltage_ranges.pop()
        else:
            self.voltage_range = None

        if len(temperature_ranges) == 1:
            self.temperature_range = temperature_ranges.pop()
        else:
            self.temperature_range = None


    def __str__(self):
        return f"{self.name}: Voltage Range: {self.voltage_range}, Temperature Range: {self.temperature_range}"
