from typing import Optional, Callable

import ftrack_api

from ftrack_undo.proxy import proxy_inject


def ftrack_session_log_inject(session: ftrack_api.Session,
                              logging_function: Optional[Callable] = None) -> None:
    session.call = proxy_inject(session.call, post_function=logging_function)


