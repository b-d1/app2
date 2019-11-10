# -*- coding: utf-8 -*-
"""Create an application instance."""
import logging
from flask import request
from app2.app import create_app


app = create_app()


@app.before_request
def request_logging():
    message = 'Request URL: {}\nRequest Method: {}\nRequest data: {}\nRemote IP: {}\nRemote User-Agent: {}'.format(
        request.url, request.method, request.data.decode(), request.remote_addr, request.headers.get('User-Agent'))
    logger = logging.getLogger('request')
    logger.log("INFO", message)


@app.after_request
def response_logging(response):
    message = 'Response status: {}\nResponse content: {}'.format(
        response.status, [x.decode() for x in response.response])
    logger = logging.getLogger('response')
    logger.log("INFO", message)
    return response
