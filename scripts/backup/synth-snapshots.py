"""
Backs each synth snapshot patch up to OP1.fun
"""
import os

from tqdm import tqdm

from src.utils.device import is_connected
from src.utils.audio import to_base64
from src.services.op1_dot_fun.api import create_patch, get_my_patches

if not is_connected():
    raise RuntimeError("OP-1 is not connected.")

print("Backing up synth snapshots...")

# Get patches that are already backed up
backed_up_patches = [
    f'{patch["attributes"]["name"]}.aif'
    for patch in get_my_patches()]

# Get patches from the device
local_patches = os.listdir("/Volumes/OP1/synth/snapshot")

# Filter out patches that are already backed up
needs_backup = [
    patch for patch in local_patches
    if patch not in backed_up_patches]

if not needs_backup:
    print("No patches need to be backed up.")
else:
    for patch in tqdm(needs_backup):
        create_patch(
            name=patch.replace(".aif", ""),
            public=False,
            base64_encoded_audio_file=to_base64(
                f"/Volumes/OP1/synth/snapshot/{patch}"))

    print("Done!")
