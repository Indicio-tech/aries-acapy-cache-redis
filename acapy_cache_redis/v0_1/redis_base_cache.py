import logging
from aries_cloudagent.core.profile import Profile
from aries_cloudagent.cache.base import BaseCache
from typing import Any, Sequence, Text, Union

import aioredis
import ssl
import json

LOGGER = logging.getLogger(__name__)


class RedisBaseCache(BaseCache):
    """Redis Base Cache."""

    config_key = "redis_cache"

    def __init__(self, root_profile: Profile) -> None:
        """Initialize the cache instance."""
        LOGGER.debug("Initializing Redis Base Cache")
        super().__init__()
        # looks like { "key": { "expires": <epoch timestamp>, "value": <val> } }
        """Set initial state."""
        username = None
        password = None
        ca_cert = None
        context = ssl._create_unverified_context()
        try:
            plugin_config = root_profile.settings["plugin_config"] or {}
            config = plugin_config[self.config_key]
            self.connection = config["connection"]
        except KeyError as error:
            raise OutboundQueueConfigurationError(
                "Configuration missing for redis queue"
            ) from error
        try:
            plugin_config = root_profile.settings["plugin_config"] or {}
            config = plugin_config[self.config_key]
            credentials = config["credentials"]
            username = credentials["username"]
            password = credentials["password"]
        except KeyError as error:
            pass
            # raise OutboundQueueConfigurationError(
            #     "Configuration missing for redis queue"
            # ) from error
        try:
            plugin_config = root_profile.settings["plugin_config"] or {}
            config = plugin_config[self.config_key]
            lssl = config["ssl"]
            ca_cert = lssl["cacerts"]
        except KeyError as error:
            pass
            # raise OutboundQueueConfigurationError(
            #     "Configuration missing for redis queue"
            # ) from error

        self.prefix = config.get("prefix", "acapy")
        self.pool = aioredis.ConnectionPool.from_url(
            self.connection, max_connections=10,
            username=username, password=password,
            ssl_ca_certs=ca_cert,
        )
        self.redis = aioredis.Redis(connection_pool=self.pool)

    async def get(self, key: Text):
        """
        Get an item from the cache.

        Args:
            key: the key to retrieve an item for

        Returns:
            The record found or `None`

        """
        response = await self.redis.get(f"ACA-Py:{key}")
        if response is not None:
            response = json.loads(response)
        return response
        pass
    async def set(self, keys: Union[Text, Sequence[Text]], value: Any, ttl: int = None):
        """
        Add an item to the cache with an optional ttl.

        Args:
            keys: the key or keys for which to set an item
            value: the value to store in the cache
            ttl: number of second that the record should persist

        """
        #TODO: set redis cache given a key
        LOGGER.debug("set:%s value:%s ttl:%d", keys, value, ttl)
        # self._remove_expired_cache_items()
        # expires_ts = time.perf_counter() + ttl if ttl else None
        for key in [keys] if isinstance(keys, Text) else keys:
            # self._cache[key] = {"expires": expires_ts, "value": value}
            await self.redis.set(f"ACA-Py:{key}", json.dumps(value), ex=ttl)



    async def clear(self, key: Text):
        """
        Remove an item from the cache, if present.

        Args:
            key: the key to remove

        """
        keysDeleted = await self.redis.delete(f"ACA-Py:{key}")

    async def flush(self):
        """Remove all items from the cache."""
        await self.redis.delete(f"ACA-Py:*")