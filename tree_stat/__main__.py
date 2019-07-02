#!/usr/bin/env python3
import argparse
import logging
import os
from tempfile import mkdtemp
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape

from tree_stat import directory_measure as dm
from tree_stat._formatter import COMMERCIAL, INFORMATICS, format_file_size, path_formatter

log = logging.getLogger(__name__)


def tree_stat(directory, must_print=None, output=None, light=False, pov=None):
    directory_measures = take_measures(directory)

    env = Environment(
        loader=PackageLoader('tree_stat', 'templates'),
        autoescape=select_autoescape(['md']),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals['format_file_size'] = lambda size: format_file_size(size, args.coefficient_base)
    env.globals['pov_formatter'] = path_formatter(directory, pov)

    if light:
        template = env.get_template('tree_stat_light.md')
    else:
        template = env.get_template('tree_stat.md')

    report = template.render(directory_measures=directory_measures)

    if must_print or not output:
        print(report)
    if output:
        try:
            output.write_text(report)
        except PermissionError:
            tmp_dir = mkdtemp(prefix='tree_stat_')
            replacement_path = Path(tmp_dir, output.name)
            replacement_path.write_text(report)
            log.error('Permission to write to {} was denied, wrote to {} instead'.format(output, replacement_path))


def take_measures(directory):
    measures = []

    stack = []
    for current, sub_dirs, files in os.walk(str(directory), topdown=False):
        log.debug('working in {}'.format(current))

        measure = dm.DirectoryMeasure(files, path=Path(current))
        measures.insert(0, measure)

        log.debug('own measure: {}'.format(measure))

        if stack and stack[-1].parent == measure.path:
            measure.eat(stack.pop())
            log.debug('child fed measure: {}'.format(measure))

        if stack and stack[-1].parent == measure.parent:
            stack[-1].eat(measure)
        else:
            stack.append(measure.edible_clone())

    return measures


def main():
    global args
    parser = argparse.ArgumentParser(description='Find files recursively and compute size of each directory level')
    parser.add_argument('directory', type=Path, nargs='?', default=Path.cwd().relative_to(Path.cwd()),
                        help='a directory to search in')
    parser.add_argument('-o', '--output', type=Path, help='File to write to result into')
    parser.add_argument('--print', dest='must_print', default=False, action='store_true',
                        help='Print result to standard output, it is the default if --output is not specified')
    parser.add_argument('--commercial-base', dest='coefficient_base', default=INFORMATICS, action='store_const',
                        const=COMMERCIAL, help='By default, size is printed using coefficient with base 1024.'
                                               ' This option sets coefficient base to 1000')
    parser.add_argument('--verbose', default=False, action='store_true', help='Display debug logs')
    parser.add_argument('--point-of-view', '--pov', dest='pov', default=None, choices=['target', 'root', 'parent'],
                        help='set the point of view to display the path with')
    parser.add_argument('--type-without-path', dest='light', default=False, action='store_true',
                        help='Do not repeat path in front of file type record')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)

    tree_stat(args.directory, must_print=args.must_print, output=args.output, light=args.light, pov=args.pov)


if __name__ == '__main__':
    main()
