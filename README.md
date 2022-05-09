# acapy-cache-redis
Redis Base Cache Plugin
=======================================

[Add description]

## Installation and Usage

First, install this plugin into your environment.

```sh
$ poetry install
$ poetry shell
$ aca-py start --arg-file ./docker/default.yml
```

When starting up ACA-Py, load the plugin along with any other startup
parameters.

```sh
$ aca-py start --arg-file ./docker/default.yml
```
## Running Tests for development

```sh
pytest --cov-report term-missing --cov
```