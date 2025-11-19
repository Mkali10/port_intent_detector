# setup
from setuptools import setup, find_packages

setup(
    name="port-intent-detector",
    version="0.1.0",
    description="A small tool that monitors outbound connections and infers intent based on port",
    author="Mkali10",
    url="https://github.com/Mkali10/port_intent_detector",
    packages=find_packages(),
    install_requires=[
        "psutil>=5.0"
    ],
    entry_points={
        "console_scripts": [
            "port-intent = port_intent_detector.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
