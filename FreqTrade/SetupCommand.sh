!/bin/bash

# Install pre-requisite packages
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