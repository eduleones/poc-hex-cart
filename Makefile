export PYTHONPATH=$(shell pwd)/src/
export PYTHONDONTWRITEBYTECODE=1
export ENVIRONMENT=DEVELOPMENT

.PHONY=help


help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## Remove cache files
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf


###
# Dependencies section
###
_base_pip:
	@pip install -U pip wheel poetry

_base_poetry:
	@poetry install


dev-dependencies: _base_pip _base_poetry ## Install development dependencies

ci-dependencies: _base_pip
	@poetry export --without-hashes --dev -f requirements.txt > requirements.txt
	@pip install -r requirements.txt

dependencies: _base_pip ## Install dependencies
	@poetry install --no-dev

outdated: ## Show outdated packages
	@poetry show --outdated


###
# Lint section
###
_flake8:
	@flake8 --show-source .

_isort:
	@isort --diff --check-only src/

_black:
	@black --check src/

_isort-fix:
	@isort .

_black_fix:
	@black .

_dead_fixtures:
	@pytest --dead-fixtures tests/

_mypy:
	@mypy src/

pre-commit:
	@pre-commit run --all-files

lint: _flake8 _isort _black _mypy _dead_fixtures   ## Check code lint
format-code: _isort-fix _black_fix ## Format code


###
# Tests section
###
test: clean ## Run tests
	@pytest tests/ -n auto

test-coverage: clean ## Run tests with coverage output
	@pytest tests/ --cov src/ --cov-report term-missing --cov-report xml --cov-report html -n auto

test-debug: clean ## Run tests with active pdb
	@pytest -s -x tests/

test-matching: clean ## Run tests by match ex: make test-matching k=name_of_test
	@pytest -s -k $(k) tests/

test-security: clean ## Run security tests with bandit and safety
	@python -m bandit -r src -x "test"
	@python -m safety check



###
# Run section
###
run:  ## Run server with default settings
	@gunicorn src.main:app -b 0.0.0.0:8000 --keep-alive 5 --preload -k uvicorn.workers.UvicornWorker --workers 4 --log-level debug

run-dev: ## Run server with development settings
	@uvicorn src.main:app --host="0.0.0.0" --port=8000 --reload
