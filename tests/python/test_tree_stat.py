from tree_stat.__main__ import tree_stat
from pathlib import Path
from shutil import rmtree


def teardown():
    tree_stat_dirs = list(d for d in Path('/tmp').iterdir() if d.name.startswith('tree_stat') and d.joinpath(
        'very-improbable-string-that-user-will-not-use.md').is_file())
    for d in tree_stat_dirs:
        rmtree(str(d))


def test_tree_stat(sample_tree_path):
    tree_stat(sample_tree_path, output=Path('/very-improbable-string-that-user-will-not-use.md'))
    tmp_dir = Path('/tmp')
    found, *others = list(d for d in tmp_dir.iterdir() if d.name.startswith('tree_stat') and d.joinpath(
        'very-improbable-string-that-user-will-not-use.md').is_file())

    assert found
    assert len(others) == 0, 'Found more than one replacement directory, did you fail to cleanup previous test ?'
    rmtree(found)
