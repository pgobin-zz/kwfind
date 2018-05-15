'''Extensible directory search.

This module contains functions for searching directories.

Example:
    Search the directory "test" for files containing the pattern
    ^[a-zA-Z]+_TESTResult.*:

        $ python kwfind.py test/ ^[a-zA-Z]+_TESTResult.*
'''

import pkgutil

# Abort module load if missing dependencies
if pkgutil.find_loader('tqdm') is None:
    sys.exit('Package "tqdm" not installed.\nRun:\t$ pip install tqdm')

import sys
import re

from os import path, walk
from tqdm import tqdm

def kwfind(root_dir, keyword):
    '''Keyword find

    Find all files in a directory and its subdirectories that match a
    given pattern expression.

    Args:
        root_dir: Directory to search
        keyword: Pattern xpression

    Returns:
        Dictionary with matching subdirectories as key and count of
        matches found as value.
    '''

    # Validate directory
    if not path.isdir(root_dir):
        print('Invalid directory.')
        return None

    # Validate pattern
    try:
        re.compile(keyword)
    except re.error:
        print('Invalid pattern expression.')
        return None

    counts = {}

    # Depth-first walk through directory with progress
    for root, dir, files in tqdm(walk(root_dir)):
        for file in files:
            if re.match(keyword, file):
                key = path.relpath(root, root_dir)
                counts[key] = counts.get(root, 0) + 1

    # Print human-readable counts
    print('{} found'.format(len(counts)))
    for x in counts:
        print('{0}: {1}'.format(x, counts[x]))

    return counts

if __name__ == '__main__':
    import argparse

    DESCRIPTION = 'Find all files in a directory that match an expression.'
    ROOT_DIR_HELP = 'Root directory to search.'
    KEYWORD_HELP = 'Pattern expression.'

    # Create argument parser
    parser = argparse.ArgumentParser(description = DESCRIPTION) 
    parser.add_argument('root_dir', help = ROOT_DIR_HELP)
    parser.add_argument('keyword', help = KEYWORD_HELP)

    args = parser.parse_args()

    # Call kwfind(...) if invoked from shell
    kwfind(args.root_dir, args.keyword)
