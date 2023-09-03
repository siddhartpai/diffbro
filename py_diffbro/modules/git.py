from typing import List
from .cmd import run_shell_command


def get_git_diff(only: List[str], ignore: List[str], branch: str = None):
    """
    Returns the git diff as a string
    If ignore is specified, diffs all files except those with those extensions
    If only is specified, only diffs files with those extensions
    If neither are specified, diffs all files
    """
    if ignore:
        print(f"Diffing ALL files except those with extensions {ignore}")
        files = " ".join(f":(exclude)'**/*{ext}'" for ext in ignore)
        command = f"git diff {branch + ' ' if branch else ''}-- . {files}"
    elif only:
        print(f"Diffing exclusively files with extensions {only}")
        files = " ".join(f"'**/*{ext}'" for ext in only)
        command = f"git diff {branch + ' ' if branch else ''}-- {files}"
    else:
        print(f"Diffing all files (no extensions specified))")
        command = f"git diff {branch + ' ' if branch else ''}--"
    return run_shell_command(command)
