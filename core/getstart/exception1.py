import os
import sys

p = 'E:\PluralSight\Python\core\larger\note.txt'

#Look before you leap
if os.path.exist(p):
    process_file(p)
    ### many issues:
    # atomicity - just after the check the file is removed
    # if it exists, but is a folder instead of a file
    # file exist, but contain only garbage
else:
    print(f'No such file as - {p}')


#EAFP - easier to ask for fogiveness than permission
try:
    process_file(p)
except (OSError) as e:
    print(f'Error: {e}')

def make_art(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    try:
        os.mkdir(dir_name)
    except (OSError) as e:
        print(e, file=sys.stderr)
        raise
    final:
        os.chdir(original_path)

