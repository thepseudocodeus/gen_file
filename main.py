import os
# import sys [] TODO: consider removing
import typer
from pathlib import Path
# from typing import Tuple

app = typer.Typer()


def generate_random_file(filename: str, size_bytes: int):
    """
    Generates a file of random binary data of the provided size.

    Args:
        filename (str): The name of the file to create. Note: Path not accepted.
        size_bytes (int): The desired size of the file in bytes.
    """
    # Ensure filename is string. (Note: I believe python types are not run time enforced.)
    if isinstance(filename, Path):
        filename = str(filename)

    print(f"Generating file: {filename} with size: {size_bytes} bytes")
    try:
        with open(filename, 'wb') as fout:
            chunk_size = 1024 * 1024 * 10 # 10 MB chunks
            while size_bytes > 0:
                bytes_to_write = min(size_bytes, chunk_size)
                fout.write(os.urandom(bytes_to_write))
                size_bytes -= bytes_to_write
        print(f"Success: {filename} created.")
    except IOError as e:
        print(f"Error: {e}. File not created. Try again.")


def build_filename(base: str, ext: str) -> str:
    """
    Uses string interpolation to generate a filename with extension.

    Args:
        base (str): core part of file name
        ext (str): file extension

    Returns:
        filename (str): {base}.{ext}
    """
    return f"{base}.{ext}"


def get_file_inputs() -> str | int:
    """
    Obtains user responses.

    Args:
        None
    """
    valid_exts = ["txt", "bin", "csv", "yaml", "json"]
    # 1. Get filename
    basename = input(f"What is the file name? ")
    ext = input(f"What file extentions? ")
    if basename == "":
        basename = "default"

    if ext not in valid_exts:
        ext = valid_exts[0]

    # 2. Make filename
    filename = build_filename(basename, ext)

    # 3. Get file size
    file_size_mb = input(f"What file size? ")
    try:
        file_size_mb = int(file_size_mb)
    except Exception as e:
        print(f"Invalid number entered: {e}")
        print("Using default 10MB")
        file_size_mb = 10
    return filename, file_size_mb


@app.command()
def run():
    """
    Example usage: Generate a 100 MB file named 'random_data.bin'
    100 MB = 100 * 1024 * 1024 bytes
    """
    file_name, file_size_mb = get_file_inputs()
    # file_name = 'random_data.bin'
    # file_size_mb = 100
    file_size_bytes = file_size_mb * 1024 * 1024

    generate_random_file(file_name, file_size_bytes)


if __name__ == "__main__":
    app()
