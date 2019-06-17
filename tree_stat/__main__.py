#!/usr/bin/env python3
import argparse
import logging
import os
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape

from tree_stat import directory_measure as dm
from tree_stat._display_file_size import COMMERCIAL, INFORMATICS, display_file_size

log = logging.getLogger(__name__)


def tree_stat(directory):
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

    if args.print or not args.output:
        print(report)
    if args.output:
        args.output.write_text(report)


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
    parser.add_argument('directory', type=Path, nargs='?', default=Path.cwd(), help='a directory to search in')
    # parser.add_argument('-e', '--extensions', nargs='+', metavar='extension', required=False,
    #                     help='only count files with these extensions')
    parser.add_argument('-o', '--output', type=Path, help='File to write to result into')
    parser.add_argument('--print', default=False, action='store_true',
                        help='Print result to standard output, it is the default if --output is not specified')
    parser.add_argument('--commercial-base', dest='coefficient_base', default=INFORMATICS, action='store_const',
                        const=COMMERCIAL, help='By default, size is printed using coefficient with base 1024.'
                                               ' This option sets coefficient base to 1000')
    parser.add_argument('--verbose', default=False, action='store_true', help='Display debug logs')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)

    tree_stat(args.directory)


if __name__ == '__main__':
    main()
