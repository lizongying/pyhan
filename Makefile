.PHONY: all

all:  test run

test:
	python -m src.test.han

run:
	python -m src.pyhan.han