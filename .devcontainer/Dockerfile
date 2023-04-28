ARG VARIANT="3.11-bullseye"

FROM "mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}"

RUN pipx install pre-commit

ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install -U \
    pip \
    setuptools \
    poetry \
    yapf \
    bandit \
    pycodestyle \
    pydocstyle \
    toml

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends ruby-full shellcheck

RUN gem install mdl
