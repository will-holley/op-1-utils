"""
Utilities for working with the physical OP-1 device.
"""
import os


def is_connected() -> bool:
    """
    Returns whether the OP-1 is connected to the computer.

    Returns:
        Whether the OP-1 is connected to the computer.
    """
    return "OP1" in os.listdir("/Volumes")
