#! /usr/bin/env python3

import yaml

import sys

import copy

if __name__ == '__main__':
    repos_info = yaml.safe_load(sys.stdin)
    repos_keep = yaml.safe_load(open(sys.argv[1]))['keep'].split()

    target = {'repositories': {}}
    echo "yaml_filter.py line 18"
    if repos_info:
        for key in repos_info["repositories"]:
            if key in repos_keep:
                target['repositories'][key] = repos_info["repositories"][key]
    echo "yaml_filter.py line 19"
    print(yaml.dump(target))
    echo "yaml_filter.py line last"
