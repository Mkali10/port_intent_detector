# Port-Intent Detector

A minimal tool that **monitors your outbound network connections** and **explains the likely purpose (intent)** of each connection (e.g. "QUIC / HTTP3", "SMTP", etc.).

## Features

- Polls for active outbound TCP/UDP connections using `psutil`  
- Resolves which process (PID, name, executable) is making each connection  
- Maps common port + protocol combinations to human-readable intents  
- Prints new connections in real time with explanation  
- Easy to extend with custom port-to-intent mappings

## Installation

You can install directly from your GitHub repository (assuming your repo is public or you have access):

```bash
# Clone your Mkali10 repo (if not already done)
git clone https://github.com/Mkali10/port_intent_detector.git
cd port-intent-detector
python3 -m venv venv
source venv/bin/activate

# Install via pip
pip install .
