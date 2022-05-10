# acapy-cache-redis
Redis Base Cache Plugin
=======================================

[Add description]

## Installation and Usage

First, install this plugin into your environment.

```sh
$ poetry install
$ poetry shell
```

Local redis server is for development.

```sh
$ docker run -v /redis.conf:/usr/local/etc/redis --name redis_cache redis redis-server /usr/local/etc/redis/redis.conf
```

When starting up ACA-Py, load the plugin along with any other startup
parameters.

```sh
$ aca-py start --arg-file ./docker/default.yml
```

For manual testing with a second ACA-Py instance, you can run the following.

```sh
$ aca-py start --arg-file ./docker/default.yml --admin 0.0.0.0 3003 -it http 0.0.0.0 3002 -e http://localhost:3002 
```

## Running Tests for development

```sh
pytest --cov-report term-missing --cov
```