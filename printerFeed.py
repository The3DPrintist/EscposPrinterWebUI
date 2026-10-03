import requests
import time
from escpos.printer import Usb
from flask import Flask, request, jsonify
from flask_cors import CORS
# Documentation for escpos: https://python-escpos.readthedocs.io/en/latest/index.html

# --- CONFIGURATION ---
# Replace with your actual printer details
# the vendor id of epson is 0x04b8, you can also supply product id if you want a specific model only, but this SHOULD catch all the models of TM88s. If it wont print, look here first.
VENDORID = 0x04b8
#PRODUCTID = 0x0202

# --- INITIALIZATION ---
try:
    # Initialize the printer using escpos library
    printer = Usb(VENDORID)
    #printer = Usb(VENDORID,PRODUCTID)
except Exception as e:
    print(f"Could not connect to printer. Error: {e}")
    printer = None

def print_text(text):
    print("-" * 20)
    print(text)
    print("-" * 20)
    if printer is not None:
        printer.set(align='left')
        printer.text(text)
        printer.cut()

        #some more ideas:
        #printer.set(align='left')
        #printer.text("Hello World\n")
        #printer.image("logo.gif")
        #printer.barcode('4006381333931', 'EAN13', 64, 2, '', '')
        #printer.cut()


app = Flask(__name__)
CORS(app)

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json

    print("Received:", data)
    print_text(data["message"])

    # Do whatever you want with it
    # print(data["message"])

    return jsonify({"success": True})


app.run(host="127.0.0.1", port=5000)

if __name__ == "__main__":
    main()
