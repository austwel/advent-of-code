all:
	$(foreach file, $(filter-out 00.py, $(wildcard *.py)), python3 $(file);)

%:
	python3 $@.py $(d)

new:
	cp 00.py $(d).py
