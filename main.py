#!/usr/bin/env python3
import os
import re
import subprocess

from Adafruit_IO import Client
from dotenv import load_dotenv


load_dotenv()

ADAFRUIT_AIO_USERNAME = os.getenv('ADAFRUIT_AIO_USERNAME')
ADAFRUIT_AIO_KEY = os.getenv('ADAFRUIT_AIO_KEY')

NAME = os.getenv('NAME', '').lower()

MACOS = os.getenv('MACOS', 'False') == 'True'

FEED = f'{NAME}-cpu-temperature'


def get_cpu_temperature_linux():
    """Get CPU temperature (GNU/Linux version)."""
    with open('/sys/class/hwmon/hwmon0/device/temp') as f:
        temp = f.read()

    return int(temp) / 1000


def get_cpu_temperature_macos():
    """Get CPU temperature (macOS version)."""
    powermetrics_command = [
        'sudo',
        'powermetrics',
        '--samplers', 'smc',
        '--sample-count', '1'
    ]

    cp = subprocess.run(
        powermetrics_command,
        capture_output=True,
        encoding='utf-8'
    )
    if cp.returncode != 0:
        raise Exception('powermetrics: Failure')

    v = cp.stdout.split('\n')
    for s in v:
        m = re.search(r'^CPU die temperature: ([0-9]+\.?[0-9]*) C$', s)
        if m is not None:
            break
    if m is None:
        raise Exception('search: Failure')

    return float(m.group(1))


if MACOS:
    get_cpu_temperature = get_cpu_temperature_macos
else:
    get_cpu_temperature = get_cpu_temperature_linux


aio = Client(ADAFRUIT_AIO_USERNAME, ADAFRUIT_AIO_KEY)

cpu_temperature = get_cpu_temperature()

print(f'{cpu_temperature} \260C')

feed = aio.feeds(FEED)
aio.send_data(feed.key, cpu_temperature)
