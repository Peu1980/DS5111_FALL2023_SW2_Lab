default:
	@cat makefile

env:
	python3 -m venv env
	. env/bin/activate; pip install -r requirements.txt
	#. env/bin/activate; python -m pip install pytest

show:
	. env/bin/activate; pip list
run:
	@. env/bin/activate; python3 bin/clockdeco_param.py

#Code to get ALWAYS called the following task even though the tests directory exists
.PHONY: tests

tests:
	. env/bin/activate; pytest -vv tests



