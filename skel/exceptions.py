from flask import Response, jsonify


class HTTPException(Exception):
    message = ""
    status_code = 500

    def __init__(self, message, status_code, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message
        self.status_code = status_code

    def response(self):
        return Response(self.message, status=self.status_code)


class JSONException(Exception):
    message = {}
    status_code = 500

    def __init__(self, message, status_code, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message
        self.status_code = status_code

    def response(self):
        return jsonify(self.message), self.status_code


def errohandler(err):
    return err.response()
