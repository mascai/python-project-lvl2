import json
import gendiff.views as format
from gendiff.diff import generate_diff


def test_json():
    print(json.loads(generate_diff(
        "./fixtures/1__before.json", "./fixtures/1__after.json", format.json,
    )))

test_json()

