import os
import threading
from typing import List
from component import Component

class ComponentCollection:
    def __init__(self) -> None:
        self.components: List[Component] = []

    def read_component_files(self, folder_path: str) -> None:
        # Implement threading to read files concurrently
        threads = []
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            thread = threading.Thread(target=self._read_component_file, args=(filepath,))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()

    def _read_component_file(self, filepath: str) -> None:
        # Read the content of the file and create Component objects
        with open(filepath, 'r') as file:
            content = file.readlines()
            component_name = os.path.splitext(os.path.basename(filepath))[0]  # Extract component name from filename
            component = Component(component_name)
            content = ''.join(content)  # Concatenate lines to form a single string
            component.parse_ranges(content)
            self.components.append(component)

    def get_components_for_conditions(self, voltage: float, temperature: float) -> List[Component]:
        # Return components that can operate under given conditions
        compatible_components: List[Component] = []
        for component in self.components:
            if component.voltage_range and component.temperature_range:
                if component.voltage_range[0] <= voltage <= component.voltage_range[1] \
                        and component.temperature_range[0] <= temperature <= component.temperature_range[1]:
                    compatible_components.append(component)
        return compatible_components
