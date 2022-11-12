# syntax=docker/dockerfile:1.3-labs
FROM jupyter/scipy-notebook

RUN pip install aiohttp==3.8.*

# spacy
RUN <<EOF
	pip install -U setuptools wheel
	pip install -U spacy==3.4.*
	python -m spacy download en_core_web_sm
EOF

# nltk
RUN <<EOF
	pip install --user -U nltk==3.7
	pip install --user -U numpy==1.23.*
EOF

RUN python -m pip install --upgrade pymupdf==1.20.*
RUN pip install fastcoref==2.0.*

# coreferee
RUN <<EOF
	pip install spacy-transformers
	python3 -m pip install coreferee==1.3.*
	python3 -m coreferee install en
	python -m spacy download en_core_web_lg
	python -m spacy download en_core_web_trf
EOF


