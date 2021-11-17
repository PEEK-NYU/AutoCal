LINTER = flake8
API_DIR = API
DB_DIR = db
REQ_DIR = .
PYDOC = python3 -m pydoc -w
TESTFINDER = nose2

export TEST_MODE = True

FORCE:

tests: lint unit

unit: FORCE
	$(TESTFINDER) --with-coverage

lint: FORCE
	$(LINTER) *.py

docs: FORCE
	$(PYDOC) ./*.py
	git add ./*.html