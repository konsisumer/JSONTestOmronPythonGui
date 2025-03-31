# JSON Test Omron Python GUI

## Overview
This project is a Python-based graphical user interface (GUI) application built with `tkinter`. It allows users to send and receive JSON data to/from a server. The application provides a user-friendly interface for inputting data, sending it as JSON, and displaying server responses.

## Features
- **Send JSON Data**: Users can input specific parameters and send them as JSON to a server.
- **Dynamic Input Fields**: Predefined fields allow users to customize the JSON data.
- **Status Messages**: Displays server responses or error messages in a dedicated status box.
- **Error Handling**: Handles invalid inputs and network errors gracefully.

---

## JSON Structure

### JSON Sent to the Server
The application sends JSON data with the following structure:

```json
{
  "JobID": 1,
  "JobName": "ExampleName",
  "A": 80.0,
  "B": 25.0,
  "C": 15.0,
  "BoxType": 1,
  "Orientation": true,
  "Smallbox": false,
  "La": 190,
  "Lb": 150,
  "Lc": 110,
  "Enable": true,
  "Chars": 16,
  "Pos": 1,
  "Corner": 1,
  "Flap": 1,
  "DistanceStart": 8,
  "DistanceHeight": 8,
  "Lines": 2,
  "EmptyLines": 0,
  "NumMatrices": 8
}
```

#### Field Descriptions:
- **JobID**: Integer representing the job ID (default: `1`).
- **JobName**: String representing the name of the job (e.g., "ExampleName").
- **A, B, C**: Float values representing specific parameters (e.g., dimensions or measurements).
- **BoxType**: Integer indicating the type of box.
- **Orientation**: Boolean indicating the orientation of the object (`true` or `false`).
- **Smallbox**: Boolean indicating whether the object is a small box.
- **La, Lb, Lc**: Integer values representing lengths or dimensions.
- **Enable**: Boolean indicating whether Braille is enabled.
- **Chars**: Integer representing the number of Braille characters.
- **Pos**: Integer representing the position of Braille text.
- **Corner**: Integer representing the corner type.
- **Flap**: Integer representing the flap type.
- **DistanceStart**: Integer representing the starting distance.
- **DistanceHeight**: Integer representing the height distance.
- **Lines**: Integer representing the number of lines.
- **EmptyLines**: Integer representing the number of empty lines.
- **NumMatrices**: Integer representing the number of matrices.

### JSON Received from the Server
The application expects the server to return a JSON response, which is displayed in the status box. The structure of the response depends on the server implementation.

---

## Project Structure
```
JSONTestOmronPythonGui
├── src
│   ├── gui.py          # Main GUI application
│   └── utils
│       └── helpers.py  # Helper functions for sending JSON data
├── tests
│   └── test_gui.py     # Unit tests for the GUI
├── .gitignore           # Git ignore file
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── LICENSE              # License information
```

---

## Installation

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/JSONTestOmronPythonGui.git
   ```
2. Navigate to the project directory:
   ```bash
   cd JSONTestOmronPythonGui
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running the Application
1. Start the application:
   ```bash
   python src/gui.py
   ```
2. Enter the server URL in the input field (default: `http://192.168.250.1:8080/`).
3. Use the input fields to configure the JSON data to send.
4. Click **Send Data** to send the JSON to the server.
5. View the server's response or error messages in the status box.

### GUI Overview
- **URL Input**: Enter the server URL for sending JSON data.
- **Input Fields**: Configure the JSON data to send using labeled input fields.
- **Send Data Button**: Sends the configured JSON data to the server.
- **Status Messages**: Displays server responses or error messages.

---

## Testing
Unit tests are provided in the `tests/test_gui.py` file. To run the tests:
```bash
python -m unittest discover tests
```

---

## Dependencies
The project requires the following Python packages:
- `tkinter`: For creating the GUI.
- `random` and `string`: For generating random strings.
- `utils.helpers`: Custom helper functions for sending JSON data.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Open a pull request with a detailed description of your changes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Screenshots
### Main GUI
![Main GUI](https://via.placeholder.com/800x600?text=Main+GUI+Screenshot)

---

## Acknowledgments
- Built with Python and `tkinter`.
- Inspired by the need for a simple JSON data sender and viewer.

---
Feel free to open an issue or submit a pull request if you encounter any problems or have suggestions for improvement.