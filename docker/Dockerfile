#FROM bcgovimages/von-image:py36-1.16-1
FROM ghcr.io/hyperledger/aries-cloudagent-python:py3.9-0.9.0-rc0

USER root 
ENV POETRY_HOME=/opt/poetry \
    VENV=/usr/src/app/.venv
ENV PATH="$POETRY_HOME/bin:$VENV/bin:$PATH"

# RUN curl -sSL https://install.python-poetry.org | python -
# Fixes installation failure
RUN pip3 install --no-cache-dir poetry
RUN poetry config virtualenvs.create true; poetry config virtualenvs.in-project true

RUN mkdir acapy_cache_redis && touch acapy_cache_redis/__init__.py
COPY --chown=root:root README.md setup.py pyproject.toml poetry.lock ./

RUN poetry install --no-dev

# Make site packages location more accessible (for use with volumes)
RUN ln -s $(poetry env info -p)/lib/python3.6/site-packages site-packages

COPY --chown=root:root docker/default.yml .
COPY --chown=root:root acapy_cache_redis/ acapy_cache_redis/

ENTRYPOINT ["/bin/bash", "-c", "poetry run aca-py \"$@\"", "--"]
CMD ["start", "--arg-file", "default.yml"]
