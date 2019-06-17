from collections import defaultdict
from os.path import splitext
from pathlib import Path
import logging

log = logging.getLogger('tree_stat.dm')


class DirectoryMeasure:
    def __init__(self, files, path=None, parent=None):
        self.path = path
        self.parent = parent if parent is not None else path.parent
        self.file_type_measures = defaultdict(FilesMeasure)

        for f in (Path(f) for f in files):
            ext = splitext(f)[1]
            file_size = path.joinpath(f).stat().st_size
            self.file_type_measures[ext].volume += file_size
            self.file_type_measures[ext].count += 1

    @property
    def total(self):
        it = FilesMeasure()
        for v in self.file_type_measures.values():
            it.volume += v.volume
            it.count += v.count
        return it

    def eat(self, child):
        for ext, v in child.file_type_measures.items():
            self.file_type_measures[ext].volume += v.volume
            self.file_type_measures[ext].count += v.count

    def edible_clone(self):
        clone = DirectoryMeasure([], parent=self.path.parent)
        clone.eat(self)
        return clone

    def __repr__(self):
        return 'DirectoryMeasure({})' \
            .format(', '.join(['{v}={{{v}}}'
                              .format(v=v) for v in vars(self).keys()])) \
            .format(**vars(self))


class FilesMeasure:
    def __init__(self):
        self.volume = 0
        self.count = 0

    def __repr__(self):
        return 'FilesMeasure({})' \
            .format(', '.join(['{v}={{{v}}}'
                              .format(v=v) for v in vars(self).keys()])) \
            .format(**vars(self))
