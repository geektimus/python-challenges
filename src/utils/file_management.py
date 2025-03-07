# File I/O operations

def read_file(file_path):
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