#!/bin/bash
echo "[*] Installing dependencies..."
pip install pycryptodome requests

echo "[*] Setting up module..."
# Fix .so naming for Python import
SO_FILE=$(find . -name "de.cpython*.so" 2>/dev/null | head -1)
if [ -n "$SO_FILE" ]; then
    cp "$SO_FILE" "de.so"
    echo "[+] Module ready: de.so"
else
    echo "[!] No .so file found!"
    exit 1
fi

echo "[*] Setup complete! Run: python run.py"
