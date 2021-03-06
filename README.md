# iot2aps-lambda

This is AWS Lambda implementation of IoT Rule Action that sends iot data to AMP (Amazon Managed Service for Prometheus).

Architecture

![architecture](doc/2022-04-03-10-59-54.png)


Grafana Dashboard

![Grafana Dashboard](doc/2022-04-03-11-03-08.png)


## MQTT Payload

```json
{
  "temperature": 20.1,
  "humidity": 60.5,
  "pressure": 1024
}
```


## Prerequired

* Python 3.9
* AWS CLI
* AWS SAM CLI


## How to Use

### get src

```
git clone https://github.com/moritalous/iot2aps-lambda.git
```

### build

```
cd iot2aps-lambda/iot2aps-lambda/
```

```
sam build
```

### deploy

```
sam deploy --guided
```

Property values below

| Guide | Setting value | example |
| --- | --- | --- |
| Parameter WorkspaceIdParameter | Prometheus Workspace ID | ws-05871e4c-f715-4877-b880-fa1bda971965 |
| Parameter MetricsNameParameter | Prometheus Metrics Name (`__name__`) | sensor_metrics |
| Parameter TopicParameter | IoT Rule Action Topic Name | topic/sensor |


Creating AWS Resource

| LogicalResourceId | ResourceType |
| --- | --- |
| IoT2ApsFunctionIoTRulePermission | AWS::Lambda::Permission |
| IoT2ApsFunctionIoTRule | AWS::IoT::TopicRule |
| IoT2ApsFunctionRole | AWS::IAM::Role |
| IoT2ApsFunction | AWS::Lambda::Function |

# Test

* create `.env` file in tests directory

```
WORKSPACE_ID=ws-05871e4c-f715-4877-b880-fa1bda971965
METRICS_NAME=sensor_metrics
AWS_REGION=ap-northeast-1
```

* run pytest

in iot2aps-lambda directory

```
PYTHONPATH=iot2aps/ python3.9 -m pytest
```

# Reference

I reference this gist. Thanks you @robskillington .

https://gist.github.com/robskillington/fb82ee5c737b79a3bc891df3dce7a9aa
