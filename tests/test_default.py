import gendiff.views as format
from gendiff.diff import generate_diff

def test_default():
    with open('./tests/fixtures/1__expected_default.txt', 'r') as fixture:
        expected = fixture.read()

        assert expected == generate_diff(
            './tests/fixtures/1__before.json',
            './tests/fixtures/1__after.json',
            format.default,
        )
        assert expected == generate_diff(
            "./tests/fixtures/2__before.yaml",
            './tests/fixtures/2__after.yaml',
            format.default,
        )
        assert expected == generate_diff(
            './tests/fixtures/1__before.json',
            './tests/fixtures/2__after.yaml',
            format.default,
        )


def test_nested_default():
    with open('./tests/fixtures/3__expected.txt', 'r') as fixture:
        expected = fixture.read()
        assert expected == generate_diff(
            './tests/fixtures/3__before.json',
            './tests/fixtures/3__after.json',
            format.plain,
        )