install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C *.py

test: 
	python3.10 -m pytest -vv --cov=data_generator test_data.py

# Define Variables
PAPERNOTEBOOKS = $(wildcard *.ipynb)
OUTPUT_DIR = executed_notebooks

# Ensure the output directory exists before running Papermill
$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

register-kernel:
	@echo "--- Registering ipykernel for Papermill ---"
	# Installs the kernel specification for the current environment as 'python3'
	# Note: ipykernel must be installed in the environment prior to this step.
	python -m ipykernel install --user --name=python3 --display-name "Python 3"

# Target to execute all notebooks using Papermill for testing
test_notebooks: $(OUTPUT_DIR)
	@echo "--- Batch executing all Jupyter notebooks... ---"
	# Iterate over each notebook found and run Papermill
	for notebook in $(PAPERNOTEBOOKS); do \
		echo "Executing $$notebook -> $(OUTPUT_DIR)/executed_$$notebook"; \
		papermill "$$notebook" "$(OUTPUT_DIR)/executed_$$notebook"; \
	done
	@echo "--- All notebooks successfully executed and saved to $(OUTPUT_DIR)/ ---"

# Clean up all generated files and directories
clean:
	@echo "--- Cleaning up generated files... ---"
	rm -rf $(OUTPUT_DIR)

all: install lint test test_notebooks clean
