import logging
from typing import Optional, Callable

from wrapt import ObjectProxy


def proxy_inject(function: Callable,
                 pre_function: Optional[Callable] = None,
                 post_function: Optional[Callable] = None,
                 extra_data: Optional[dict] = dict) -> ObjectProxy:
    class CallableWrapper(ObjectProxy):
        def __call__(self, *args, **kwargs):
            if pre_function:
                logger.debug('proxy_inject_pre_function: {} {}'.format(args, kwargs))
                pre_function(*args, **kwargs)
            try:
                result = self.__wrapped__(*args, **kwargs)
                if post_function:
                    logger.debug('proxy_inject_post_function: {}, {}'.format(args, kwargs))
                    post_function(result, *args, **kwargs)
                return result
            except Exception as e:
                raise e

    logger = logging.getLogger(__name__)
    return CallableWrapper(function)
