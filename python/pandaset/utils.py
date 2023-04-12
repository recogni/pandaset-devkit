#!/usr/bin/env python3
import os
from typing import List
import fsspec

def subdirectories(directory: str, fs: fsspec.AbstractFileSystem = None) -> List[str]:
    """List all subdirectories of a directory.

    Args:
        directory: Relative or absolute path

    Returns:
        List of path strings for every subdirectory in `directory`.
    """
    if fs is None:
        return [d.path for d in os.scandir(directory) if d.is_dir()]
    else:
        return [fs.protocol[0] + "://" + d for d in fs.ls(directory) if fs.isdir(d)]

if __name__ == '__main__':
    pass
