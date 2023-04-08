import os
import subprocess
import sys

def install_exiftool():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'exiftool'])
    except subprocess.CalledProcessError:
        print('Failed to install exiftool')
        sys.exit(1)

if __name__ == '__main__':
    install_exiftool()

    try:
        os.remove(__file__)
    except OSError:
        print(f'Failed to delete {__file__}')

    print('exiftool installed and script deleted.')
