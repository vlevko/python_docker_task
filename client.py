#!/usr/bin/env python

import argparse
import time
import threading
import requests
from requests.exceptions import HTTPError
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Simple HTTP client to request JSON data from localhost \
            listening port 1234 and serving /api/data route'
    )
    parser.parse_args()


def _requests_retry_session():
    retry = Retry(
        total=2,
        connect=2,
        read=2,
        status_forcelist=(429,),
        backoff_factor=0.2,
    )
    session = requests.Session()
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    return session

def _get():
    print(time.ctime())
    try:
        response = _requests_retry_session().get('http://127.0.0.1:1234/api/data')
        response.raise_for_status()
        json_response = response.json()
        print(json_response)
    except HTTPError as HTTP_error:
        print(HTTP_error)
    except Exception as error:
        print(error)
    threading.Timer(600, _get).start()


def _main():
    _parse_args()
    _get()


if __name__ == '__main__':
    _main()
