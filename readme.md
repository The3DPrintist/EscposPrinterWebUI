# Webpage Receipt Printing System

A Python-based service that receives data from a webpage and automatically prints it via a USB thermal printer using the `python-escpos` library.

## Features
- **Automatic Polling:** Automatically fetches data from a defined URL at a configurable interval.
- **ESC/POS Support:** Utilizes the `python-escpos` library to handle standard thermal printer commands (cutting paper, text alignment, etc.).
- **Robust Connections:** Includes error handling for both network requests and printer connectivity issues.

## Prerequisites
Before running the script, ensure you have the following:
- Python 3.x installed.
- A USB Thermal Printer connected to your machine.
- Access to the `escpos` library (which requires some system dependencies like `libusb`).

## Installation

1. **Clone or download** this repository.
2. **Install dependencies:**
   ```bash
   pip install python-escpos[all]
   ```
   ```bash
   pip install requests
   ```
   ```bash
   pip install flask
   ```
   ```bash
   pip install flask_cors
   ```
3. **System Dependencies:**
   Depending on your OS, you may need to install `libusb` (e.g., `sudo apt-get install libusb-dev` on Linux).

## Configuration

Open `printerFeed.py` and modify the following variables in the **CONFIGURATION** section:

| Variable | Description |
| :--- | :--- |
| `VENDORID` | The ID of your printer (default is set to `0x04b8` for Epson). |
| `PRODUCTID` | (Optional) Specific product ID if you have multiple printers from the same vendor. |

## Usage

Run the script from your terminal:

```bash
python printerFeed.py
```

Open the HTML file, (or run locally, which may be required to make CORS happy)
The html file will have a text box and send button, which allows you to send any text to the printer on the webpage.