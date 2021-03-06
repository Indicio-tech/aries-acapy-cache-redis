__version__ = "0.1.0"


import logging
import os

from aries_cloudagent.cache.base import BaseCache
from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.protocols.problem_report.v1_0.message import ProblemReport

from .redis_base_cache import RedisBaseCache

LOGGER = logging.getLogger(__name__)


async def setup(context: InjectionContext):
    """Load Redis Base Cache Plugin."""
    LOGGER.debug("Loading Redis Base Cache Plugin")
    context.injector.bind_instance(BaseCache, RedisBaseCache(context))


__all__ = ["ProblemReport"]
