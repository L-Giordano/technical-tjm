
VENV = .venv

REQ = requirements.txt

POST_AMOUNT ?= 10

vitual-env:
	python3 -m venv $(VENV)

install:
	. $(VENV)/bin/activate && pip install -r $(REQ)

clean:
	rm -rf $(VENV)

create_resource_folder:
	mkdir resource

setup: vitual-env install create_resource_folder

run:
	. $(VENV)/bin/activate && python script.py $(POST_AMOUNT)

all: setup install