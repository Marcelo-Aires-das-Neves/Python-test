import sys
from sayings import goodbye, hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
