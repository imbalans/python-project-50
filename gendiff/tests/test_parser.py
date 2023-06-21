from gendiff import parser
import pytest
from gendiff.tests import test_formaters


@pytest.mark.parametrize("file_name1,file_name2", [("file1.json", "file1.yaml"), ("file2.json", "file2.yml")])
def test_pars(file_name1, file_name2):
    assert parser.load_and_select_formatter(
        test_formaters.build_fixture_path(file_name1)) == parser.load_and_select_formatter(
        test_formaters.build_fixture_path(file_name2))
