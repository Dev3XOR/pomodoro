all: format lint test

clean:
	rm -rf ./dist/*
	rm -rf ./src/*.egg-info

lint:
	pylint --rcfile="./setup.cfg" ./src ./tests

format:
	black ./src

test:
	coverage run -m unittest -v
	coverage report --show-missing
	coverage html

build:
	python -m build

publish: build
	python -m twine upload --repository testpypi dist/*
