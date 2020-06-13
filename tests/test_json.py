import json
import gendiff.views as format
from gendiff.diff import generate_diff


def test_json():
    with open("./tests/fixtures/1__expected.json", "r") as f:
        expected = json.load(f)
        assert expected == json.loads(generate_diff(
            "./tests/fixtures/1__before.json", "./tests/fixtures/1__after.json", format.json,
        ))
        assert expected == json.loads(generate_diff(
            "./tests/fixtures/2__before.yaml", "./tests/fixtures/2__after.yaml", format.json,
        ))
