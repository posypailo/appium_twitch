# Appium Twitch Automation Project

This project contains automated tests for the Twitch application using Appium and Python. The tests are designed to run on both Android and iOS devices.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your local machine
- Appium server installed and running
- Android or iOS emulator/device configured for testing
- Required dependencies installed (listed in `requirements.txt`)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/appium_twitch.git
    cd appium_twitch
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the Appium server:

    ```bash
    appium
    ```

4. Configure your device or emulator, and ensure it is connected.

## Running the Tests

To run the tests locally, execute the following command:

```bash
pytest
```

## Project Structure

The repository follows a well-organized structure to separate different aspects of the test automation framework. Below is the directory structure:

```
appium_twitch/
├── tests/
├── twitch/
│ ├── components/
│ ├── configs/
│ ├── constants/
│ ├── pages/
│ │ └── android/
│ ├── screenshots/
│ ├── utils/
│ │ ├── elementsActions/
│ │ └── waits/
```

### Description of the Structure:

- **`tests/`**: Contains the test scripts that execute the automation tests. Each test is structured to validate specific functionalities of the Twitch application.

- **`twitch/`**: The core folder of the project, containing the main components and utilities necessary for test automation.

  - **`components/`**: Holds reusable components or modules that can be shared across different pages.

  - **`configs/`**: Contains configuration files for setting up the environment, capabilities, and other project-specific configurations.

  - **`constants/`**: Stores constant values that are used throughout the project, such as global variables, URLs, or timeouts.

  - **`pages/`**: This folder follows the Page Object Model (POM) pattern, with classes representing different pages of the Twitch application.

    - **`android/`**: Contains Android-specific page objects. These classes define the locators and actions that can be performed on Android devices.

  - **`screenshots/`**: This folder is where screenshots are saved during test execution, typically used for debugging or reporting.

  - **`utils/`**: Contains utility classes and functions that support the tests and page objects.

    - **`elementsActions/`**: Utility methods for interacting with single or multiple elements, such as clicking, sending keys, or verifying states.

    - **`waits/`**: Contains wait utility classes to handle waiting for elements to be present, visible, or clickable, improving the reliability of the tests.