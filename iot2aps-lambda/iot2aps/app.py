import calendar
import logging
import os
from datetime import datetime

import botocore.session
import requests
import requests_aws4auth
import snappy

from remote_pb2 import WriteRequest
from types_pb2 import Label, Labels, Sample, TimeSeries

workspace_id=os.environ['WORKSPACE_ID']
metrics_name=os.environ['METRICS_NAME']

service = 'aps'
region = os.environ['AWS_REGION']
host = '{service}-workspaces.{region}.amazonaws.com'.format(service=service, region=region)
endpoint = 'https://{host}/workspaces/{workspace_id}/api/v1/remote_write'.format(host=host, workspace_id=workspace_id)
content_type = 'application/x-protobuf'

headers = {
    'Content-Type':content_type,
    'Content-Encoding': 'snappy',
    'X-Prometheus-Remote-Write-Version': '0.1.0',
    'User-Agent': 'Prometheus/2.20.1'
}

def create_body(thing_name, timestamp, data):
    write_request = WriteRequest()

    for key in data.keys():
        val = data[key]

        series = write_request.timeseries.add()

        # name label always required
        label = series.labels.add()
        label.name = "__name__"
        label.value = "iot_metrics"
        
        # as many labels you like
        label = series.labels.add()
        label.name = "thing_name"
        label.value = thing_name

        # as many labels you like
        label = series.labels.add()
        label.name = "sensor"
        label.value = key

        sample = series.samples.add()
        sample.value = val
        sample.timestamp = timestamp 

    uncompressed = write_request.SerializeToString()
    compressed = snappy.compress(uncompressed)

    return compressed


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        IoT Core Input Format

    context: object, required
        Lambda Context runtime methods and attributes
    """

    print(event)

    auth = requests_aws4auth.AWS4Auth(
                refreshable_credentials=botocore.session.Session().get_credentials(),
                region=region, service=service)

    thing_name = event['thing_name']
    payload = event['payload']
    timestamp = event['timestamp']
    body = create_body(thing_name, timestamp, payload)

    response = requests.post(endpoint, headers=headers, auth=auth, data=body)

    print(response.status_code)
    print(response.content)

    return {
        "statusCode": response.status_code
    }
