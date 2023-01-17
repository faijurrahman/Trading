#!/bin/bash

# Please following this guide to prepare Ubuntu in windows WSL
# Guide: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps

# Step1: Related commands in Power shell
# wsl --update
# wsl --shutdown

# Step2: Then ubuntu commands to install all necessary packages
# sudo apt update
# sudo apt install gedit -y
# sudo apt install gimp -y
# sudo apt install nautilus -y
# sudo apt install x11-apps -y
# sudo apt install geany -y

# Step 3: To install the Google Chrome for Linux:
# Change directories into the temp folder: cd /tmp
# Use wget to download it: sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# Get the current stable version: sudo dpkg -i google-chrome-stable_current_amd64.deb
# Fix the package: sudo apt install --fix-broken -y
# Configure the package: sudo dpkg -i google-chrome-stable_current_amd64.deb


# Install pre-requisite packages for freqtrade
sudo apt-get update
sudo apt-get install python3
sudo apt install -y python3-pip
sudo apt install -y python3-venv
sudo apt install -y python3-dev
sudo apt install -y python3-pandas

# Download stable source code from github
git clone https://github.com/freqtrade/freqtrade.git
cd freqtrade/
git checkout stable

# Setup the freqtrade binaries
./setup.sh -i

# Activate venv
source ./.env/bin/activate

# Create user_data and config.json
freqtrade create-userdir --userdir user_data
freqtrade new-config --config config.json

# Download data
freqtrade download-data --config config.json --days 999 -t 5m 15m 30m 1h