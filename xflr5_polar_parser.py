#!/user/bin/env python3
"""
This script is used to parser XFLR5 polar files.
It has been tested with XFLR5 v6.09.06.

Copyright Rebecca Li 2018
robot@seas.upenn.edu
"""

# Imports
import sys
#import os

# Global variables

# Class declarations

# Function declarations

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--flags options] [inputs] ')
        sys.exit(1)

# Main body
if __name__ == '__main__':
    main()
