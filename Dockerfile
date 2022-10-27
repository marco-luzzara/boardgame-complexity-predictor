# syntax=docker/dockerfile:1.3-labs
FROM jupyter/scipy-notebook

RUN pip install aiohttp

# spacy
RUN <<EOF
pip install -U setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
EOF

# nltk
RUN <<EOF
pip install --user -U nltk
pip install --user -U numpy
EOF

RUN python -m pip install --upgrade pymupdf
