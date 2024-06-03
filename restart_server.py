#!/usr/bin/python3
import requests
import subprocess
import sys


def stop_server():
    subprocess.run(["pkill", "python3"], capture_output=False)


def run_server():
    try:
        res = subprocess.run(["python3", "-m", "api.v1.app"],
                             text=True, capture_output=False)
    except KeyboardInterrupt:
        print()
        stop_server()



try:
    # response = requests.get("http://0.0.0.0:5000/api/v1/states")
    stop_server()
    run_server()
except requests.ConnectionError:
    run_server()
    sys.exit(0)
