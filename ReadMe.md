# QR Code Generator with Styled Features

## Overview
This Python script generates a **highly customized QR code** with:
- **Rounded module edges** for a smooth, modern look  
- **Gradient color styling** for an aesthetic touch  
- **Embedded logo** at the center for branding  

---

## 🔹 Features
✅ Uses the `qrcode` library to generate QR codes  
✅ Applies **RoundedModuleDrawer** for stylish edges  
✅ Uses **RadialGradiantColorMask** for gradient effects  
✅ **Overlays a custom logo** at the center of the QR code  
✅ **Ensures versioning**, so QR codes don’t get overwritten  

---

## 🛠️ Requirements
Before running the script, install the necessary dependencies:

## For Linux & MacOS
```bash
    # Create a virtual environment (recommended)
    python3 -m venv myenv
    source myenv/bin/activate

    # Install dependencies
    pip install qrcode pillow
```
## For Windows
```bash
    # Create a virtual environment (recommended)
    python -m venv myenv
    myenv\Scripts\activate



    # Install dependencies
    pip install qrcode pillow
```

## How to Use the Script  

## 1. Edit the URL  
Modify the `url` variable inside the script to point to the desired website or resource.  

## 2. Prepare Your Logo  
- Place your logo image (`logo.png`) in the same directory as the script.  
- If your logo is **transparent**, the script automatically adds a **white background** to ensure visibility.  

## 3. Run the Script  
### For Linux & MacOS
```bash
python3 main.py
```
### For Windows
```bash
myenv\Scripts\activate     
python main.py
```
