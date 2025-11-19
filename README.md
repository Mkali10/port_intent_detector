# Port-Intent Detector

A minimal tool that **monitors your outbound network connections** and **explains the likely purpose (intent)** of each connection (e.g. "QUIC / HTTP3", "SMTP", etc.).

## Features

- Polls for active outbound TCP/UDP connections using `psutil`  
- Resolves which process (PID, name, executable) is making each connection  
- Maps common port + protocol combinations to human-readable intents  
- Prints new connections in real time with explanation  
- Easy to extend with custom port-to-intent mappings

## Run on Windows
Go to Git for Windows
https://git-scm.com/install/windows
Download the installer (Git-2.52.0-64-bit.exe) and run it.
Keep default options unless you know what you’re doing.
Make sure “Git from the command line” is selected.
- Verify installation:
git --version

## Clone your GitHub repository
Open Command Prompt.
Navigate to the folder where you want to clone for example cd C:\Users\<YourUser>\Documents
Clone your repo using HTTPS:- git clone https://github.com/Mkali10/port-intent-detector.git
Go inside the cloned folder: 
- cd port-intent-detector
- RUN  python -m venv venv
Activate it with venv\Scripts\activate

Install dependencies and your package
Install your project editable: 
pip install -e .

This tells Python to use your local code as a package.

If you added psutil in install_requires in setup.py, pip will automatically install it.
port-intent



## Installation (Linux)

You can install directly from your GitHub repository (assuming your repo is public or you have access):

```bash
# Clone your Mkali10 repo (if not already done)
git clone https://github.com/Mkali10/port_intent_detector.git
cd port-intent-detector
python3 -m venv venv
source venv/bin/activate

# Install via pip
pip install .

# Run 
port-intent



