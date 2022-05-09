import logging
from aries_cloudagent.cache.base import BaseCache
from typing import Any, Sequence, Text, Union

LOGGER = logging.getLogger(__name__)


class RedisBaseCache(BaseCache):
    """Redis Base Cache."""

    def __init__(self):
        """Initialize the cache instance."""
        LOGGER.debug("Initializing Redis Base Cache")
        super().__init__()
        # looks like { "key": { "expires": <epoch timestamp>, "value": <val> } }

    async def get(self, key: Text):
        """
        Get an item from the cache.

        Args:
            key: the key to retrieve an item for

        Returns:
            The record found or `None`

        """
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
        LOGGER.debug("set:", keys, value, ttl)

    async def clear(self, key: Text):
        """
        Remove an item from the cache, if present.

        Args:
            key: the key to remove

        """
        #TODO: clear redis cache given a key
        pass

    async def flush(self):
        """Remove all items from the cache."""
        pass