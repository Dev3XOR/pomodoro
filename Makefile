all: format lint test

lint:
	pylint --rcfile="./setup.cfg" ./src ./tests

format:
	black ./src

test:
	coverage run -m unittest -v
	coverage report --show-missing
	coverage html
