clean:
	rm -rf venv
	find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf

venv/bin/activate: requirements.txt
	@echo "Activating virtual environment and installing dependencies"
	python3 -m venv venv && \
    . venv/bin/activate && \
    ./venv/bin/pip install -r requirements.txt

install: venv/bin/activate
	@echo "Installing stopwords for preprocessing."
	./venv/bin/python3 -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('wordnet')"

run: venv/bin/activate install
	@echo "Running server"
	./venv/bin/python3 src/main.py

test:
	./venv/bin/python3 src/test.py
