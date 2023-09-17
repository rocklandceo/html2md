#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Navigate to the parser directory and install its dependencies
cd parser
npm install
