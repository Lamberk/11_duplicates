import os
import argparse


GLOBAL_DICTIONARY = dict()


def get_files(file_path):
    files_set = set()
    for root, subdirs, files in os.walk(file_path):
        if files:
            files_set.update(
                {
                    '{}.{}'.format(
                        file,
                        os.stat(os.path.join(root, file)).st_size,
                    ) for file in files
                }
            )
            for file in files:
                GLOBAL_DICTIONARY['{}.{}'.format(
                    file,
                    os.stat(os.path.join(root, file)).st_size,
                )] = os.path.join(root, file)
    return files_set


def find_duplicates(file_path1, file_path2):
    first_set = get_files(file_path1)
    second_set = get_files(file_path2)
    dupl_files = [GLOBAL_DICTIONARY[file] for file in first_set & second_set]
    if dupl_files:
        print('Duplicates found: ', dupl_files)
    else:
        print('No duplicates found')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p1',
        '--path1',
        help='Path to first folder',
        required=True,
    )
    parser.add_argument(
        '-p2',
        '--path2',
        help='Path to second folder',
        required=True,
    )
    args = parser.parse_args()
    find_duplicates(args.path1, args.path2)
