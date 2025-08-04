"""
Simple nextcloud curl check for monitoring or adjusting weights
"""

import os
import requests


def check() -> int:
    """
    check if the nextcloud instance is good
    """
    # Get the token from an environment variable
    token = os.getenv("NC_TOKEN")
    if not token:
        raise ValueError(
            "You need to set your nextcloud monitoring token in order to use this check"
        )

    url = "http://127.0.0.1/ocs/v2.php/apps/serverinfo/api/v1/info?format=json"

    headers = {"NC-token": token}

    # Make the GET request
    try:
        response = requests.get(url, headers=headers, timeout=10)
    except requests.exceptions.Timeout:
        print("request timed out")
        return 1  # we don't know what's up with the instance, haproxy should notice by itself if it's not available

    if response.status_code // 100 == 2:
        return 100
    elif response.status_code // 100 == 5:
        return 0
    elif response.status_code == 401:
        raise ValueError("Your token is invalid")
    elif response.status_code == 404:
        raise ValueError("Your administrator did not install the monitoring app")
    else:
        raise ValueError(f"Unknown nextcloud status {response.status_code}")


if __name__ == "__main__":
    print(f"Status: {check()}%")
