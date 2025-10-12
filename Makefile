install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C *.py

test: 
	python3.10 -m pytest -vv --cov=data_generator test_data.py

test_ipynb: 
	papermill k_means_diagnostics.ipynb /tmp/output.ipynb
	papermill k_means_analysis.ipynb /tmp/output2.ipynb

all: install lint test test_ipynb