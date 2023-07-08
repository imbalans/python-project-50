from gendiff import parser
import pytest
from tests import test_formaters


@pytest.mark.parametrize("file_name1,file_name2", [("file1.json", "file1.yaml"), ("file2.json", "file2.yml")])
def test_pars(file_name1, file_name2):
    assert parser.read_file(
        test_formaters.build_fixture_path(file_name1)) == parser.read_file(
        test_formaters.build_fixture_path(file_name2))
