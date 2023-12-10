"""
Utilities for working with audio files.
"""
import base64


def to_base64(file_path: str) -> str:
    """
    Converts a file to base64 encoded string.

    Args:
        file_path: The path to the file to convert.
    Returns:
        The base64-encoded file.
    """
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")
