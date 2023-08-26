install:
	echo "Installing dependencies..."
	pip install --upgrade pip 
	pip install -r requirements.txt
	echo "Done Installing."

lint:
	echo "Linting..."
	pylint --disable=R,C src/*.py
	echo "Done Linting."

test:
	@echo "Running tests..."
	python -m unittest discover -s src
	@echo "Done running tests."

run:
	@echo "Running..."
	python src/main.py
	@echo "Done running."


