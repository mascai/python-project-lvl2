install:
	poetry install
test:
	poetry run pytest -vv --cov=gendiff --cov-report xml tests/
lint:
	poetry run flake8 gendiff
