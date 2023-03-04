ARG VARIANT="3.11-bullseye"

FROM "mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}"

RUN pipx install poetry \
    && pipx install pre-commit

ENV POETRY_VIRTUALENVS_CREATE=true

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends ruby-full shellcheck

RUN gem install mdl
