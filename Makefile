.PHONY: format lint lint-fix quality fix test

format:
	black .

lint:
	ruff check .

lint-fix:
	ruff check --fix .

quality: format lint

fix: format lint-fix

test:
	poetry run pytest