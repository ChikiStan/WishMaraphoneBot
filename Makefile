.PHONY: default venv lint pretty dev-start dev-build

default:
	@echo "There is no default target."

venv:
	rm -rf venv
	python -m venv venv
	pip install -r requirements.txt

lint:
	black --check -l 79 app
	flake8 --extend-ignore=E501,E292,F401,W291 app
	isort -c --src app app

pretty:
	black -l 79 app
	flake8 app
	isort -c --src app app

dev-start:
	docker-compose -f deployments/docker-compose.dev.yml up

dev-build:
	docker-compose -f deployments/docker-compose.dev.yml build --no-cache
