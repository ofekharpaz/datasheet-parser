import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from component import Component  # Relative import from parent directory

class TestComponent(unittest.TestCase):
    def test_parse_ranges_valid(self):
        # Test case for valid input with both voltage and temperature ranges
        text = "Voltage Range: 1.2V to 3.5V, Temperature Range: -40°C to 85°C"
        component = Component("TestComponent")
        component.parse_ranges(text)
        self.assertEqual(component.voltage_range, (1.2, 3.5))
        self.assertEqual(component.temperature_range, (-40, 85))

    def test_parse_ranges_no_temp(self):
        # Test case for missing temperature range
        text = "Voltage Range: 1.2V to 3.5V"
        component = Component("TestComponent")
        component.parse_ranges(text)
        self.assertIsNone(component.temperature_range)
        
    def test_parse_ranges_no_voltage(self):
        # Test case for missing temperature range
        text = "Temperature Range: -40°C to 85°C"
        component = Component("TestComponent")
        component.parse_ranges(text)
        self.assertIsNone(component.voltage_range)
        
    def test_parse_ranges_multiple_voltage_ranges(self):
        # Test case for input with multiple voltage ranges
        text = "Voltage Range: 1.2V to 3.5V, Voltage Range: 4.0V to 6.0V, Temperature Range: -40°C to 85°C"
        component = Component("TestComponent")
        component.parse_ranges(text)
        self.assertIsNone(component.voltage_range)  # Multiple voltage ranges, should be set to None
        self.assertEqual(component.temperature_range, (-40, 85))

if __name__ == "__main__":
    unittest.main()