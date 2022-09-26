# End to End Web3 Application
# Introduction
Web3 technology is inherently about the user controlled internet. It is being achieved by a growing stack of decentralized technologies, such as blockchains, smart contracts, oracles, crypto wallets, storage networks, and more.
# Objective
This project tries to enable clients to be able to solve the challenges ensuring that certificates are available to all trainees in a secure way, and (if possible) that certificate holders can benefit from smart contract actions now and in the future. At present, certificates are distributed as simple PDF files, without the ability to verify their authenticity nor can trainer undertake smart actions with the trainees/their contracts.
# Development Setup
This repo requires Python 3.6 or higher. We recommend you use a Python virtual environment to install the required dependencies.

Set up venv (one time):

python3 -m venv venv
Active venv:

. venv/bin/activate (if your shell is bash/zsh)
. venv/bin/activate.fish (if your shell is fish)
Install dependencies:

pip install -r requirements.txt
Run tests:

First, start an instance of sandbox (requires Docker): ./sandbox up nightly
pytest
When finished, the sandbox can be stopped with ./sandbox down
Format code:

black .
