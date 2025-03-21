# JSON Test Omron Python GUI

## Overview
This project is a Python application with a graphical user interface (GUI) that allows fetching and sending JSON data. Users can interact with a server, display data in a tabular format, and send data through a user-friendly interface.

## Project Structure
```
JSONTestOmronPythonGui
├── src
│   ├── gui.py          # Main GUI code of the application
│   └── utils
│       └── helpers.py  # Helper functions for data fetching and sending
├── tests
│   └── test_gui.py     # Unit tests for GUI functions
├── .gitignore           # Files and directories ignored by Git
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── LICENSE              # License information
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/JSONTestOmronPythonGui.git
   ```
2. Navigate to the project directory:
   ```
   cd JSONTestOmronPythonGui
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Start the application:
   ```
   python src/gui.py
   ```
2. Enter the URL for fetching or sending JSON data in the input field.
3. Use the input fields to send data and view the received data in the table.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request to suggest improvements or fix bugs.

## License
This project is licensed under the MIT License. For more details, see the `LICENSE` file.