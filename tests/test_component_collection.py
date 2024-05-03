import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from component_collection import ComponentCollection

class TestComponentCollection(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "test_components"
        os.makedirs(self.test_dir, exist_ok=True)

        # Create dummy component files
        self.create_dummy_files()

        # Create a ComponentCollection object for testing
        self.component_collection = ComponentCollection()
        
        self.component_collection.read_component_files(self.test_dir)

    def create_dummy_files(self):
        # Create dummy component files in the test directory
        components_data = {
            "component1.txt": "Voltage Range: 1.2V to 3.5V, Temperature Range: -40°C to 85°C\n",
            "component2.txt": "Voltage Range: 2.0V to 5.0V, Temperature Range: -20°C to 100°C\n"
        }

        for filename, content in components_data.items():
            with open(os.path.join(self.test_dir, filename), "w") as file:
                file.write(content)

    def tearDown(self):
        # Clean up the temporary directory after tests
        if os.path.exists(self.test_dir):
            for filename in os.listdir(self.test_dir):
                filepath = os.path.join(self.test_dir, filename)
                os.remove(filepath)
            os.rmdir(self.test_dir)

    def test_read_component_files(self):
        self.assertEqual(len(self.component_collection.components), 2)  # Two dummy components added

    def test_get_components_for_conditions(self):
        # Test retrieving components for specified operating conditions
        voltage = 3.0  # Example voltage
        temperature = -30  # Example temperature
        compatible_components = self.component_collection.get_components_for_conditions(voltage, temperature)
        # Add assertions to verify that the correct components are retrieved
        self.assertEqual(len(compatible_components), 1)  # Only one component should be compatible
        
        voltage = -3.0  # Example voltage
        temperature = -30  # Example temperature
        compatible_components = self.component_collection.get_components_for_conditions(voltage, temperature)
        self.assertEqual(len(compatible_components), 0)  

if __name__ == "__main__":
    unittest.main()
