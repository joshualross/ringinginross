project := application
flake8 := flake8
pytest_args := --capture=sys --tb short --cov-config .coveragerc --cov $(project) tests
pytest := py.test $(pytest_args)

html_report := --cov-report html
test_args := --cov-report term-missing --cov-report xml --junitxml junit.xml

# All of these commands can be run with an explicit `CLAY_CONFIG=` environment
# variable to override environment settings.

.DEFAULT_GOAL := usage

.PHONY: usage
usage:
	@echo make bootstrap - install requirements
	@echo make clean - clean up the pyc files and previous test results
	@echo make lint - run the linter
	@echo make test - run the tests
	@echo make shell - python shell


.PHONY: bootstrap
bootstrap:
	pip install -r requirements-tests.txt
	pip install -r requirements.txt
	python setup.py develop 

.PHONY: test
test: clean
	$(pytest) $(test_args)

.PHONY: clean
clean:
	@find $(project) "(" -name "*.pyc" -o -name "coverage.xml" -o -name "junit.xml" ")" -delete

.PHONY: lint
lint:
	flake8 application 

.PHONY: shell
shell:
	ipython

