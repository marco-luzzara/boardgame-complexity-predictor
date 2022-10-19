FROM jupyter/scipy-notebook

RUN pip install aiohttp

# spacy
RUN <<EOF
	pip install -U pip setuptools wheel
	pip install -U spacy
	python -m spacy download en_core_web_sm
	EOF
