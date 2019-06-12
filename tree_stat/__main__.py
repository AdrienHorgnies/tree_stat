#!/usr/bin/env python3
import argparse
import logging
import os

from jinja2 import Environment, PackageLoader, select_autoescape

from tree_stat import directory_measure as dm
from tree_stat._display_file_size import COMMERCIAL, INFORMATICS, display_file_size

log = logging.getLogger(__name__)


def tree_stat(directory=None):
    directory = directory or os.getcwd()
    directory_measures = take_measures(directory)

    env = Environment(
        loader=PackageLoader('tree_stat', 'templates'),
        autoescape=select_autoescape(['md']),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals['display_file_size'] = lambda size: display_file_size(size, args.coefficient_base)

    template = env.get_template('tree_stat.md')

    report = template.render(directory_measures=reversed(list(directory_measures.values())))

    with open('tree_stat.md', 'w') as f:
        f.write(report)


def take_measures(directory):
    dir_tree = dict()

    stack = []
    for current, sub_dirs, files in os.walk(directory, topdown=False):
        log.debug('working in {}'.format(current))

        measure = dm.DirectoryMeasure(files, path=current)
        dir_tree[current] = measure

        log.debug('own measure: {}'.format(measure))

        if stack and stack[-1].parent == measure.path:
            measure.eat(stack.pop())
            log.debug('child fed measure: {}'.format(measure))

        if stack and stack[-1].parent == measure.parent:
            stack[-1].eat(measure)
        else:
            stack.append(measure.edible_clone())

    return dir_tree


def main():
    global args
    parser = argparse.ArgumentParser(description='Find files recursively and compute size of each directory level')
    parser.add_argument('directory', nargs='?', help='a directory to search in')
    # parser.add_argument('-e', '--extensions', nargs='+', metavar='extension', required=False,
    #                     help='only count files with these extensions')
    parser.add_argument('-c', '--classify', default=False, action='store_true',
                        help='Display size by file type')
    parser.add_argument('--commercial-base', dest='coefficient_base', default=INFORMATICS, action='store_const',
                        const=COMMERCIAL, help='By default, size is printed using coefficient with base 1024.'
                                               ' This option sets coefficient base to 1000')
    parser.add_argument('--DEBUG', default=False, action='store_true', help='Display debug logs')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.DEBUG else logging.INFO)

    tree_stat(args.directory)


if __name__ == '__main__':
    main()
