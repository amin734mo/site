.PHONY: all install upgrade coverage html travis test clean upload

clean:
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -type d -exec rm -rf {} \;
	find . -name "*.egg-info" -type d -exec rm -rf {} \; || true
	rm -rf coverage_html_report .coverage

install:
	pip install -U setuptools
	pip install -U html5lib
	pip install -q psycopg2
	pip install -r requirements.txt
	pip install anglerfish
	pip install css-html-js-minify

coverage:
	coverage run --source=landing,agcs runtests.py

html: coverage
	coverage html

travis: coverage

test:
	python runtests.py
