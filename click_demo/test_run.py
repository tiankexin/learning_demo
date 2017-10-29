import os
import sys
print os.path.realpath('test.py')
sys.argv = ["test.py", "cmd2", '--help']
execfile('test.py')
