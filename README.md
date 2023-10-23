# About this repo

This repository contains a Python REST API project that is designed to handle the upload and management of TXT files. The API allows users to  upload and retrieve text files in a simple and straightforward manner.

## Requirements

- Python 3.7 or higher
- Fast Api
- minio docker container

## Setup 

```bash
AWS_BUCKET_NAME=
ACCESS_KEY=
SECRET_KEY=
HOST_BUCKET=
SIGNATURE_VERSION=
RESOURCE_TYPE=
PORT=
```

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Usage

```bash
http://0.0.0.0:8000/docs
``` 

## Resources

[boto3](https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session)

[upload](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/bucket/upload_fileobj.html)

