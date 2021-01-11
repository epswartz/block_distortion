pypi: clean build
	twine upload dist/*

test_pypi: clean build
	twine upload --repository testpypi dist/*

build:
	python3 setup.py sdist

clean:
	rm -rf dist
