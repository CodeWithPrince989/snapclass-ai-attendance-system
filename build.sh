#!/usr/bin/env bash
set -e

echo "Using Python 3.11..."
python3.11 --version || python3 --version

echo "Upgrading pip, setuptools, wheel..."
python3.11 -m pip install --upgrade pip setuptools wheel 2>&1 | tail -5

echo "Installing requirements..."
python3.11 -m pip install -r requirements.txt

echo "Build complete!"
