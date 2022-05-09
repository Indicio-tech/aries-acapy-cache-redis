__version__ = "0.1.0"


import os
import logging

from aries_cloudagent.protocols.problem_report.v1_0.message import ProblemReport
from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.cache.base import BaseCache
from .redis_base_cache import RedisBaseCache


async def setup(context: InjectionContext):
    """Load Redis Base Cache Plugin."""
    log_level = os.environ.get("ACAPY_REDIS_BASE_CACHE_LOG_LEVEL", logging.WARNING)
    logging.getLogger("acapy_plugin_redis_base_cache").setLevel(log_level)
    print("Setting logging level of redis base cache to", log_level)
    context.injector.bind_instance(BaseCache, RedisBaseCache())


__all__ = ["ProblemReport"]
