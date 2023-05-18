from gendiff import gendiff


def test_gendiff():
    right_result = open("gendiff/tests/fixtures/stylish_right_result")
    right_result = right_result.read()
    assert gendiff.generate_diff('gendiff/tests/fixtures/file1.json',
                                 'gendiff/tests/fixtures/file2.json') == right_result
