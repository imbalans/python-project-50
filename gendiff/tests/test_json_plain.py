from gendiff import gendiff
import pytest

test_input_plain = gendiff.generate_diff("gendiff/tests/fixtures/file2.json", "gendiff/tests/fixtures/file1.json", "PLAIN")
right_plain = open("gendiff/tests/fixtures/plain_right_result")
right_plain = right_plain.read()
test_input_json = (gendiff.generate_diff("gendiff/tests/fixtures/file1.json", "gendiff/tests/fixtures/file2.json", "JSON"))
right_json = open("gendiff/tests/fixtures/json_right_result")
right_json = right_json.read()


@pytest.mark.parametrize("test_input,expected", [(test_input_json, right_json), (test_input_plain, right_plain)])
def test_plain_and_json(test_input, expected):
    assert test_input == expected
