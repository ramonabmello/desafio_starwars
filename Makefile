.PHONY: pip default run_tests run_app

default:
	@awk -F\: '/^[a-z_]+:/ && !/default/ {printf "- %-20s %s\n", $$1, $$2}' Makefile

pip:  ## Install production requirements
	pip install -r requirements.txt


run_tests:  ## Run the quality and unit tests
	PYTHONPATH=. pytest


run_app:  ## Run the app
	python run.py
