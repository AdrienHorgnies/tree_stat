import pytest
from pathlib import Path


@pytest.fixture()
def tests_path():
    return Path('tests')


@pytest.fixture()
def assets_path():
    return Path('tests', 'assets')


@pytest.fixture()
def sample_tree_path():
    return Path('tests', 'assets', 'sample_tree')
