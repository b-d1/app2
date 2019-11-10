import requests


def send_message(api_body):
    try:
        if 'message' in api_body:
            if api_body['message'] == 'ping':
                return {"message": "pong"}, 200
            return {"message": "app2 response"}, 200
        return {"status": "error", "reason": "no `message` key in body"}, 400
    except Exception as ex:
        print("error received")
        return {
            'error': str(ex)
        }, 400
