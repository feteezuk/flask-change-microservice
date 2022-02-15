install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
			python -m pip install requests

lint:
	pylint --disable=R,C,W1203,W0702 app.py

test:
	python -m pytest -vv --cov=app test_app.py

all: install lint test
