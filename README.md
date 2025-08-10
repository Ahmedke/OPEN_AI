# OPEN_AI

This repository contains a sample script for retrieving BGP received routes
from a Cisco IOS XR device. The script exposes a small Flask web application
that connects to the device via SSH using `scrapli` and returns the received
routes for a specified BGP peer.

## Usage

1. Install dependencies:
   ```bash
   pip install scrapli flask
   ```
2. Run the application:
   ```bash
   python iosxr_received_routes.py
   ```
3. Query the endpoint from your GUI or browser:
   ```bash
   http://localhost:5000/received_routes?host=<router_ip>&username=<user>&password=<pass>&peer=<peer_ip>
   ```
   The endpoint returns JSON describing the routes received from the given peer.
