import os
import sys
import shutil

def list_folders(directory):
    """List all folders in the given directory."""
    try:
        items = os.listdir(directory)
        folders = [item for item in items if os.path.isdir(os.path.join(directory, item))]
        return folders
    except Exception as e:
        print(f"Error accessing directory {directory}: {e}")
        return []