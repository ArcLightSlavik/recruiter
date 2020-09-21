#! /usr/bin/env python3

import os
import argh
import yaml
import shutil

# without a . on purpose
from utils import get_main_folder # noqa


def filenames_from_requirements(requirements_list):
    for item in requirements_list:
        if isinstance(item, dict):
            for partial_path, sub_items in item.items():
                for sub_item in filenames_from_requirements(sub_items):
                    yield os.path.join(partial_path, sub_item)
        else:
            yield item


def copy_files(destination=''):
    # Move files from from source_path to destination_path as specified in requirements.yaml
    requirements_filename = os.path.abspath('requirements.yaml')
    if not os.path.exists(requirements_filename):
        raise Exception(f'path {requirements_filename} not found')

    with open(requirements_filename, 'r') as file:
        requirements_list = yaml.safe_load(file)

    source_path = get_main_folder()

    if destination:
        destination_path = os.path.join(os.path.dirname(requirements_filename), destination, 'recruiter')
    else:
        destination_path = os.path.join(os.path.dirname(requirements_filename), 'recruiter')
    shutil.rmtree(destination_path, ignore_errors=True)

    for filename in filenames_from_requirements(requirements_list):
        filename = filename.strip()
        source = os.path.join(source_path, filename)
        destination = os.path.join(destination_path, filename)

        dirname = os.path.dirname(destination)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        shutil.copy(source, destination)


if __name__ == '__main__':
    argh.dispatch_command(copy_files)
