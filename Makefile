.PHONY: format lint quality test

format:
	black .

lint:
	flake8 .

quality: format lint

test:
	poetry run pytest