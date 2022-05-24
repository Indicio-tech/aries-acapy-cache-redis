FROM bcgovimages/von-image:py36-1.16-1

USER root
ENV POETRY_HOME=/opt/poetry \
    VENV=/usr/src/app/.venv
ENV PATH="$POETRY_HOME/bin:$VENV/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python -
USER indy
RUN poetry config virtualenvs.create true; poetry config virtualenvs.in-project true

RUN mkdir acapy_cache_redis && touch acapy_cache_redis/__init__.py
COPY --chown=indy:indy README.md setup.py pyproject.toml poetry.lock ./

RUN poetry install --no-dev

# Make site packages location more accessible (for use with volumes)
RUN ln -s $(poetry env info -p)/lib/python3.6/site-packages site-packages

COPY --chown=indy:indy docker/default.yml .
COPY --chown=indy:indy acapy_cache_redis/ acapy_cache_redis/

ENTRYPOINT ["/bin/bash", "-c", "poetry run aca-py \"$@\"", "--"]
CMD ["start", "--arg-file", "default.yml"]
