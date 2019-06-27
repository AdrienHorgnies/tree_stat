# noinspection PyProtectedMember
from tree_stat._formatter import COMMERCIAL, INFORMATICS, format_file_size, path_formatter
from pathlib import Path


def test_display_0():
    assert format_file_size(0, unit_base=INFORMATICS) == '0 B'
    assert format_file_size(0, unit_base=COMMERCIAL) == '0 B'


def test_display_1000():
    assert format_file_size(1000, unit_base=INFORMATICS) == '1000 B'
    assert format_file_size(1000, unit_base=COMMERCIAL) == '1.000 KB'


def test_display_1024():
    assert format_file_size(1024, unit_base=INFORMATICS) == '1.000 KiB'
    assert format_file_size(1024, unit_base=COMMERCIAL) == '1.024 KB'


def test_display_7777777():
    assert format_file_size(7777777, unit_base=INFORMATICS) == '7.417 MiB'
    assert format_file_size(7777777, unit_base=COMMERCIAL) == '7.778 MB'


def test_display_big_number():
    assert format_file_size(10 ** 100, unit_base=INFORMATICS) == '{:.3f} YiB'.format(10 ** 100 / 1024 ** 8)
    assert format_file_size(10 ** 100, unit_base=COMMERCIAL) == '{:.3f} YB'.format(10 ** 100 / 1000 ** 8)


def test_path_formatter(assets_path, sample_tree_path):
    assert path_formatter(assets_path, None)(sample_tree_path) == sample_tree_path


def test_path_formatter_target(assets_path, sample_tree_path):
    assert path_formatter(assets_path, 'target')(sample_tree_path) == Path('sample_tree')


def test_path_formatter_parent(assets_path, sample_tree_path):
    assert path_formatter(assets_path, 'parent')(sample_tree_path) == Path('assets', 'sample_tree')


def test_path_formatter_root(assets_path, sample_tree_path):
    assert path_formatter(assets_path, 'root')(sample_tree_path) == sample_tree_path.absolute()

