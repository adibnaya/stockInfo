# Stock Info Viewer

## Overview
Stock Info Viewer is a Python-based application that provides an interactive GUI for retrieving and displaying stock information from Yahoo Finance. Using the PyQt5 framework, the application offers a user-friendly interface for searching stock symbols and viewing key details such as earnings dates, PE ratios, sector, and industry data.

## Features
- **Search Functionality**: Enter a stock symbol to retrieve information from Yahoo Finance.
- **Resizable Font and Window**: Adjust the font size and window dimensions for better readability.
- **Error Handling**: Includes mechanisms to handle invalid inputs and connection timeouts.
- **Real-Time Data**: Fetches the latest stock information upon user request.

## Installation
To run Stock Info Viewer, you need to have Python installed on your system along with the PyQt5, Requests, and BeautifulSoup4 libraries.

### Prerequisites
- Python 3.x
- PyQt5
- Requests
- BeautifulSoup4

### Setting up the Environment
```bash
pip install PyQt5 requests beautifulsoup4
```

## Usage
To start the application, navigate to the project directory and run the following command:

```bash
python mainWindow.py
```

## File Structure
- `constants.py`: Contains constants used throughout the application such as base font size, window dimensions, and font settings.
- `mainWindow.py`: The main application file with the GUI setup and functionality for fetching and displaying stock data.

## Contributing
Contributions to Stock Info Viewer are welcome! Please read the contributing guidelines before submitting pull requests.

## License
This library is licensed under the MIT-0 License.
