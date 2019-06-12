# noinspection PyProtectedMember
from tree_stat._display_file_size import COMMERCIAL, INFORMATICS, display_file_size


def test_display_0():
    assert display_file_size(0, unit_base=INFORMATICS) == '0 B'
    assert display_file_size(0, unit_base=COMMERCIAL) == '0 B'


def test_display_1000():
    assert display_file_size(1000, unit_base=INFORMATICS) == '1000 B'
    assert display_file_size(1000, unit_base=COMMERCIAL) == '1.000 KB'


def test_display_1024():
    assert display_file_size(1024, unit_base=INFORMATICS) == '1.000 KiB'
    assert display_file_size(1024, unit_base=COMMERCIAL) == '1.024 KB'


def test_display_7777777():
    assert display_file_size(7_777_777, unit_base=INFORMATICS) == '7.417 MiB'
    assert display_file_size(7_777_777, unit_base=COMMERCIAL) == '7.778 MB'


def test_display_big_number():
    assert display_file_size(10 ** 100, unit_base=INFORMATICS) == '{:.3f} YiB'.format(10 ** 100 / 1024 ** 8)
    assert display_file_size(10 ** 100, unit_base=COMMERCIAL) == '{:.3f} YB'.format(10 ** 100 / 1000 ** 8)
