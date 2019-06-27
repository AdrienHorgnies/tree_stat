# noinspection PyProtectedMember
from tree_stat._formatter import COMMERCIAL, INFORMATICS, format_file_size


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
