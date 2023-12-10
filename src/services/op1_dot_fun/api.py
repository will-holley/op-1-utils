"""
Wraps the op1.fun API.
"""
import json
import os

import requests

# ========================================
# Constants
# ========================================

BASE_URL = "https://api.op1.fun/v1"

USER_EMAIL = os.environ.get("OP1_FUN_EMAIL")
API_KEY = os.environ.get("OP1_FUN_API_KEY")
USERNAME = os.environ.get("OP1_FUN_USERNAME")

if not USER_EMAIL or not API_KEY or not USERNAME:
    raise ValueError(
        "OP1_FUN_EMAIL, OP1_FUN_API_KEY, and OP1_FUN_USERNAME must be set in the environment.")

# ========================================
# Private Functions
# ========================================


def _get(endpoint: str):
    """
    Make a GET request to the OP1.fun API.

    See https://fiftyfootfoghorn.com/api.op1.fun/ for API documentation.

    Args:
        endpoint: The endpoint to GET.
    """
    return requests.get(
        f"{BASE_URL}/{endpoint}",
        headers={
            "accept": "application/json",
            "content-type": "application/json",
            "x-user-email": USER_EMAIL,
            "x-user-token": API_KEY
        })


def _post(endpoint: str, data: dict):
    """
    Make a POST request to the OP1.fun API.

    See https://fiftyfootfoghorn.com/api.op1.fun/ for API documentation.

    Args:
        endpoint: The endpoint to POST to.
        data: The data to POST.
    """
    return requests.post(
        f"{BASE_URL}/{endpoint}",
        headers={
            "accept": "application/json",
            "content-type": "application/json",
            "x-user-email": USER_EMAIL,
            "x-user-token": API_KEY
        },
        data=json.dumps(data))

# ========================================
# Public Functions
# ========================================


def get_my_patches():
    """
    Gets all of the current user's patches.
    """
    res = _get(f"users/{USERNAME}/patches")
    data = res.json()
    return data["data"]


def create_patch(name: str, public: bool, base64_encoded_audio_file: str):
    """
    Creates a new patch belonging to the current user.

    See https://fiftyfootfoghorn.com/api.op1.fun/#create-patch for API documentation.

    Args:
        name: The name of the patch.
        public: Whether the patch should be public.
        base64_encoded_audio_file: The base64-encoded audio file to upload.
    """
    res = _post("patches", {
        "data": {
            "type": "patches",
            "attributes": {
                "name": name,
                "public": public,
                "description": "",
                "license": "",
                "file": f"data:audio/x-aiff;base64,{base64_encoded_audio_file}"
            }
        }
    })

    if res.status_code != 201:
        raise RuntimeError(f"Failed to create patch: {res.text}")
