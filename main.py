from component_collection import ComponentCollection

def main():
    component_collection = ComponentCollection()

    folder_path = "Task example files"

    # Read component files
    component_collection.read_component_files(folder_path)

    # Specify operating conditions
    voltage = 5.3  
    temperature = 25
    # Get components for given conditions
    compatible_components = component_collection.get_components_for_conditions(voltage, temperature)

    # Display compatible components
    if compatible_components:
        print("Compatible Components:")
        for component in compatible_components:
            print(component)
    else:
        print("No compatible components found.")

if __name__ == "__main__":
    main()
