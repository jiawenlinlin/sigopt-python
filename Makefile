.PHONY: test lint

test:	export PYTHONPATH=.
test:
	@python -m pytest -rw -v --cov=sigopt --cov=test test

lint:
	@./lint
