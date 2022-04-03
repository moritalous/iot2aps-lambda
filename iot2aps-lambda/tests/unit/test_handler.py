import json
import time
import pytest
from dotenv import load_dotenv

load_dotenv(override=True)

import os

from iot2aps import app

@pytest.fixture()
def iotrule_event():
    """ Generates IoT Rule Event"""

    return {
            "topic": "sensor_metrics",
            "thing_name": "ThingName",
            "timestamp": int(time.time()*1000),
            "payload": {
                "temperature": 20.1,
                "humidity": 60.5,
                "pressure": 1024
            }
        }


def test_lambda_handler(iotrule_event, mocker):

    ret = app.lambda_handler(iotrule_event, "")

    assert ret["statusCode"] == 200
