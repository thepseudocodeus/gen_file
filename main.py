import os
import sys
import typer

app = typer.Typer()


def generate_random_file(filename: str, size_bytes: int):
    """
    Generates a file of a specified size filled with random binary data.

    Args:
        filename (str): The name/path of the file to create.
        size_bytes (int): The desired size of the file in bytes.
    """
    print(f"Generating file: {filename} with size: {size_bytes} bytes")
    try:
        with open(filename, 'wb') as fout:
            # Write data in chunks for very large files to manage memory
            chunk_size = 1024 * 1024 * 10 # 10 MB chunks
            while size_bytes > 0:
                bytes_to_write = min(size_bytes, chunk_size)
                # os.urandom generates random bytes
                fout.write(os.urandom(bytes_to_write))
                size_bytes -= bytes_to_write
        print(f"Successfully generated {filename}")
    except IOError as e:
        print(f"Error generating file: {e}")


def build_filename(base: str, ext: str) -> str:
    return f"{base}.{ext}"


def get_file_inputs() -> (str, int):
    """
    get_file_inputs gets user inputs
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

    # 2. Get file size
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

