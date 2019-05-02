from collections import defaultdict
from os.path import splitext, join, dirname
from os import stat


class DirectoryMeasure:
    def __init__(self, files, path=None, parent=None):
        self.path = path
        self.parent = parent or dirname(path)
        self.file_type_measures = defaultdict(FilesMeasure)
        self.count = 0
        self.volume = 0

        for f in files:
            ext = splitext(f)[1]
            self.file_type_measures[ext].volume += stat(join(path, f)).st_size
            self.file_type_measures[ext].count += 1
            self.count += 1
            self.volume += self.file_type_measures[ext].volume

    def eat(self, child):
        for ext in child.file_type_measures.keys():
            self.file_type_measures[ext].volume += child.file_type_measures[ext].volume
            self.file_type_measures[ext].count += child.file_type_measures[ext].count
            self.count += child.file_type_measures[ext].count
            self.volume += child.file_type_measures[ext].volume

    def edible_clone(self):
        clone = DirectoryMeasure([], parent=dirname(self.path))
        clone.eat(self)
        return clone

    def __repr__(self):
        return 'DirectoryMeasure(' \
               'path={path}, ' \
               'parent={parent}, ' \
               'file_type_measures={file_type_measures}, ' \
               'count={count}, ' \
               'volume={volume})'.format(
                    **vars(self)
               )


class FilesMeasure:
    def __init__(self):
        self.volume = 0
        self.count = 0

    def __repr__(self):
        return 'FilesMeasure(count={count}, volume={volume})'.format(**vars(self))
