# TaskReporter

## Overview

TaskReporter is a Python program designed to generate detailed reports about system processes and application activity on Windows. It leverages the `psutil` library to gather information about running processes, including their PID, name, user, CPU usage, and memory usage. The program outputs this information into a formatted report.

## Features

- Collects live data on system processes.
- Reports include details such as PID, process name, user, CPU usage percentage, and memory usage percentage.
- Saves the report to a text file for easy access and review.

## Requirements

- Python 3.x
- `psutil` library

You can install the `psutil` library using pip:

```bash
pip install psutil
```

## Usage

1. Clone this repository or download the `task_reporter.py` file.
2. Ensure you have Python 3.x installed on your system.
3. Install the `psutil` library if not already installed.
4. Run the script:

```bash
python task_reporter.py
```

5. The script will generate a report and save it as `system_report.txt` in the current directory.

## License

This project is open-source and available under the MIT License.