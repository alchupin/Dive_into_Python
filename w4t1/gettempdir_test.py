import tempfile
import os


with open(os.path.join(tempfile.gettempdir(), 'gettempdir.txt'), 'w') as f:
    f.write('I wrote this.')
