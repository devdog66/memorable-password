clean: 
	rm -rf dist
test:
	make clean
	python3 -m unittest
dist:
	make test
	mkdir dist
	cp words.txt dist
	cp src/classes.py dist
	cp src/memorable-password.py dist
	cp LICENSE dist
	cp README.md dist


