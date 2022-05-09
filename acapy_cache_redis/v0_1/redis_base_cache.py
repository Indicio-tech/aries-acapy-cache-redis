from aries_cloudagent.cache.base import BaseCache
from typing import Any, Sequence, Text, Union


class RedisBaseCache(BaseCache):
    """Redis Base Cache."""

    def __init__(self, redis_client):
        """Initialize the cache instance."""
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
        raise NotImplementedError

    async def set(self, keys: Union[Text, Sequence[Text]], value: Any, ttl: int = None):
        """
        Add an item to the cache with an optional ttl.

        Args:
            keys: the key or keys for which to set an item
            value: the value to store in the cache
            ttl: number of second that the record should persist

        """
        raise NotImplementedError

    async def clear(self, key: Text):
        """
        Remove an item from the cache, if present.

        Args:
            key: the key to remove

        """
        raise NotImplementedError

    async def flush(self):
        """Remove all items from the cache."""
        raise NotImplementedError

    def acquire(self, key: Text):  # not abstract
        """Acquire a lock on a given cache key."""
        raise NotImplementedError

    def release(self, key: Text):  # not abstract
        """Release the lock on a given cache key."""
        raise NotImplementedError
