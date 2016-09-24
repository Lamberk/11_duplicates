import os
import argparse
from collections import defaultdict


def get_files(file_path):
    files_dict = defaultdict(list)
    for root, subdirs, files in os.walk(file_path):
        if files:
            for file in files:
                files_dict['{}.{}'.format(
                    file,
                    os.stat(os.path.join(root, file)).st_size,
                )].append(os.path.join(root, file))
    return files_dict


def find_duplicates(file_path):
    files = get_files(file_path)
    dupl_files = [path for path in files.values() if len(path) > 1]
    if dupl_files:
        print('Duplicates found: ', dupl_files)
    else:
        print('No duplicates found')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--path',
        help='Path to folder',
        required=True,
    )
    args = parser.parse_args()
    find_duplicates(args.path)
