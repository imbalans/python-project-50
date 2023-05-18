install:
	poetry install
	poetry add flake8
	poetry add pytest-cov

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

test-cov:
	poetry run pytest --cov=gendiff --cov-report xml
