# Component Data Parser
The Component Data Parser is a Python system designed to parse component datasheet files, extract operating voltage and temperature ranges for each component, and provide functionality to retrieve components based on specified operating conditions.

## Architecture Overview
The use of Object-Oriented Programming (OOP) principles in this project allows for better organization, encapsulation, and reusability of code. The main classes utilized in this project are Component and ComponentCollection.

- **Component Class:** Represents an individual component and stores its name, voltage range, and temperature range. OOP enables us to encapsulate data and behavior related to each component within this class.

- **ComponentCollection Class:** Manages a collection of components, including reading component files, parsing data, and retrieving components based on specified operating conditions. OOP facilitates the separation of concerns and modularity, making the codebase more maintainable and extensible.
## Threading for Improved Performance
To enhance runtime efficiency, threading is employed to read component files concurrently. By utilizing threads, the system can perform file I/O operations in parallel, reducing the overall execution time. This approach is particularly beneficial when dealing with a large number of component files.

## Parsing Component Data
Regular expressions (regex) are utilized to extract operating voltage and temperature ranges from component datasheet text. Regex patterns are defined to match specific formats commonly found in datasheet text, such as "Voltage Range: 1.2V to 3.5V" and "Temperature Range: -40°C to 85°C". This approach allows for flexible and accurate parsing of range data from diverse sources.


## Unit Tests
Unit tests are implemented to verify the correctness of the system's functionality and ensure robustness against edge cases and input variations. The unittest framework is utilized to define test cases for individual components and the component collection.


## How to run

Example text files are located in the **Task example files.7z** archive. Extract the folder, then set your desired voltage and temperature conditions. Lastly, run `python main.py` to get a list of all the components that meet those restrictions.
