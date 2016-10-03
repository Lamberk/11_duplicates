import os
import argparse
from collections import defaultdict


def get_files(file_path):   
    files_dict = defaultdict(list)
    for root, subdirs, files in os.walk(file_path):
        if files:
            for single_file in files:
                files_dict['{}.{}'.format(
                    single_file,
                    os.stat(os.path.join(root, single_file)).st_size,
                )].append(os.path.join(root, single_file))
    return files_dict


def find_duplicates(files):
    return [path for path in files.values() if len(path) > 1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--path',
        help='Path to folder',
        required=True,
    )
    args = parser.parse_args()
    files = get_files(args.path)
    dupl_files = find_duplicates(files)
    if dupl_files:
        print('Duplicates found: ', dupl_files)
    else:
        print('No duplicates found')
