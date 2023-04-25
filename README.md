# WindowsRegistryMonitor.py
The script is a Python-based Windows Registry Monitor that tracks specified registry key changes, logs alterations, supports multiple keys/values, and uses a JSON config file for easy customization.


Windows Registry Monitor

This Python-based Windows Registry Monitor tracks specified registry key changes, logs alterations, supports multiple keys/values, and uses a JSON config file for easy customization.
Features

    Monitor multiple registry keys and values
    Customizable monitoring interval
    Logging of registry changes
    Easy configuration with JSON config file

Requirements

    Python 3.x
    Windows OS

Setup

    Clone the repository:

bash

git clone https://github.com/yourusername/registry-monitor.git

    Change the directory to the cloned repository:

bash

cd registry-monitor

    (Optional) Set up a virtual environment:

python -m venv venv

    Activate the virtual environment:

    On Windows:

venv\Scripts\activate

    On Linux or macOS:

bash

source venv/bin/activate

Configuration

    Open the config.json file and modify it according to your needs:

json

{
  "keys_to_monitor": [
    {
      "key": "HKEY_CURRENT_USER",
      "subkey": "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
      "value_name": "SomeValue"
    },
    {
      "key": "HKEY_CURRENT_USER",
      "subkey": "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
      "value_name": "AnotherValue"
    }
  ],
  "monitoring_interval": 5,
  "log_file": "registry_monitor.log"
}

    keys_to_monitor: An array of objects representing the registry keys and values to monitor.
        key: The main registry key (e.g., "HKEY_CURRENT_USER").
        subkey: The registry subkey path.
        value_name: The registry value name to monitor.
    monitoring_interval: The interval (in seconds) between monitoring checks.
    log_file: The name of the log file where changes will be recorded.

    Save your changes to the config.json file.

Usage

Run the registry_monitor.py script:

python registry_monitor.py

The script will start monitoring the specified registry keys and values. If any changes are detected, the script will log the information to the specified log file.

Note: Depending on the registry keys being monitored, you may need to run the script with administrative privileges.
License
