from ast import literal_eval
import base64
import requests


def plus_one(payload):
    """Adds one to the input integer."""
    try:
        return str(int(payload) + 1)
    except ValueError:
        return "Invalid input."


def sort(payload):
    """Sorts a list."""
    if payload:
        lst = literal_eval(payload)
        lst.sort()
        return str(lst)
    else:
        return "[]"


def base64_decode(payload):
    """Decodes a base64 payload."""
    return base64.b64decode(str(payload).encode()).decode()


def base64_encode(payload):
    """Encodes a base64 payload."""
    return base64.b64encode(str(payload).encode()).decode()


def to_upper(payload):
    """Converts a string to uppercase."""
    return payload.upper()


def get_server_ip(payload):
    """Gets the Lambda instance IP."""
    return requests.get("http://ipv4.icanhazip.com/").text.strip()


def fibonacci(payload):
    """Gets the nth fibonacci number"""
    try:
        if int(payload) == 0:
            return str(0)
        elif int(payload) == 1:
            return str(1)
        else:
            return str(int(fibonacci(str(int(payload) - 1))) + int(fibonacci(str(int(payload) - 2))))
    except ValueError:
        return "Invalid input."