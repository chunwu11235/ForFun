format:
	isort .
	black .

.PHONY: format

lint:
	pylint src/
	flake8 src/
	mypy src/
.PHONY: lint

test:
	pytest test/
.PHONY: test

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	rm -rf .mypy_cache
	rm -rf .pytest_cache
.PHONY: clean
