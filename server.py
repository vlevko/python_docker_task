#!/usr/bin/env python

import argparse
import random
from flask import Flask
from flask import jsonify
from flask import Response


app = Flask(__name__)


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Simple HTTP server to send JSON data or 429 response from \
            localhost port 1234 and /api/data route'
    )
    parser.parse_args()


@app.route('/api/data')
def data():
    if random.randint(0, 1):
        return jsonify()
    return Response(status=429)


def _main():
    _parse_args()
    app.run(host='127.0.0.1', port=1234, debug=True)


if __name__ == '__main__':
    _main()
