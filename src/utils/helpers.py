import requests
import json

def send_json_data(url, data):
    """
    Sends a POST request with JSON data to the specified URL.

    Args:
        url (str): The URL to send the POST request to.
        data (dict): The JSON data to include in the POST request.

    Returns:
        str: A message indicating the result of the request, based on the HTTP status code.

    HTTP Status Codes:
        - 200 OK: The request was successful.
        - 201 Created: A new resource was successfully created.
        - 202 Accepted: The request has been accepted for processing, but the processing is not complete.
        - 204 No Content: The request was successful, but no content was returned.
        - 400 Bad Request: The server could not understand the request due to invalid syntax.
        - 401 Unauthorized: Authentication is required and has failed or not been provided.
        - 403 Forbidden: The server understood the request but refuses to authorize it.
        - 404 Not Found: The requested resource could not be found.
        - 405 Method Not Allowed: The HTTP method is not allowed for the requested resource.
        - 409 Conflict: The request could not be completed due to a conflict with the current state of the resource.
        - 422 Unprocessable Entity: The request was well-formed but could not be processed due to semantic errors.
        - 500 Internal Server Error: The server encountered an unexpected condition.
        - 502 Bad Gateway: The server received an invalid response from an upstream server.
        - 503 Service Unavailable: The server is not ready to handle the request.
        - 504 Gateway Timeout: The server did not receive a timely response from an upstream server.
    """
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return "HTTP/1.1 200 OK: Request processed successfully."
    elif response.status_code == 201:
        return "HTTP/1.1 201 Created: Resource created successfully."
    elif response.status_code == 202:
        return "HTTP/1.1 202 Accepted: Request accepted for processing."
    elif response.status_code == 204:
        return "HTTP/1.1 204 No Content: Request processed successfully, no content returned."
    elif response.status_code == 400:
        return "Error: Bad Request (400)"
    elif response.status_code == 401:
        return "Error: Unauthorized (401)"
    elif response.status_code == 403:
        return "Error: Forbidden (403)"
    elif response.status_code == 404:
        return "Error: Not Found (404)"
    elif response.status_code == 405:
        return "Error: Method Not Allowed (405)"
    elif response.status_code == 409:
        return "Error: Conflict (409)"
    elif response.status_code == 422:
        return "Error: Unprocessable Entity (422)"
    elif response.status_code == 500:
        return "Error: Internal Server Error (500)"
    elif response.status_code == 502:
        return "Error: Bad Gateway (502)"
    elif response.status_code == 503:
        return "Error: Service Unavailable (503)"
    elif response.status_code == 504:
        return "Error: Gateway Timeout (504)"
    else:
        return f"Error: Unexpected status code {response.status_code}"