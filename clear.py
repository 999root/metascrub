import os
import sys
import exiftool

def clear_metadata(filename):
    with exiftool.ExifTool() as et:
        et.execute(f'-overwrite_original -all="{filename}"')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python clear.py <filename>')
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f'{filename} is not a file')
        sys.exit(1)

    clear_metadata(filename)
    print(f"Metadata cleared from {filename}")