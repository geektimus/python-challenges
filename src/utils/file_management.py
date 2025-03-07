"""
Utility functions for file operations and I/O management.

This module provides functions for reading files and handling common file-related errors.
"""

def read_file(file_path):
    """
    Read the entire contents of a file.

    Args:
        file_path (str): Path to the file to be read

    Returns:
        str: The contents of the file, or None if an error occurs
    """
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f'File not found: {file_path}')
        return None
    except Exception as e:
        print(f'Error reading file: {e}')
        return None


def read_n_lines(path, n):
    """
    Read a specific number of lines from a file.

    Args:
        path (str): Path to the file to be read
        n (int): Number of lines to read

    Returns:
        list: A list of strings, one for each line read, or None if an error occurs
    """
    try:
        with open(path) as f:
            lines = []
            for i in range(n):
                line = f.readline().strip()
                if not line:
                    break
                lines.append(line)
            return lines
    except FileNotFoundError:
        print(f'File not found: {path}')
        return None
    except Exception as e:
        print(f'Error reading file: {e}')
        return None