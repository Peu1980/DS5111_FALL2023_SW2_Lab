default:
	@cat makefile

env:
	< your code here to set up environment folder called env >
	< your code here to install packages in requirements.txt >

run:
	< your code here to call bin/clockdemo_param.py with python, and not echo the command, i.e. silently >

< your code here so the following task ALWAYS gets called, even though the directory exists >

tests:
	pytest -vv tests



