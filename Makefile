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
	./venv/bin/python3 -m nltk.downloader stopwords

run: venv/bin/activate
	@echo "Running server"
	./venv/bin/python3 src/main.py

