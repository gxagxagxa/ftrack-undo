# ftrack-undo

Add undo to ftrack Python API.

# How it works?

Inspired by MySQL undo logs, we record all transactions into logs which could be used to undo ftrack operations. It also
has some features:

- minimum impact on original ftrack python api, by proxy session.call()
- no need to class inherit
- support IDE code completion
- ship with pre-defined loggers, we can use them out of the box

# Tutorial

add undo to ftrack python api needs two steps:

1. inject log proxy into session.call(), which will record all future transactions.
2. use undo to rollback some transaction

> ⚠️ Caution!
> 
> undo could be done by datetime which is intuitive and easy, also could be done by entity and other constraints which are more complicated. 
> 
> Do it carefully!


## inject logger into session
we keep minimum impact on original ftrack python api, so it should be OK for any ftrack version (tested with ftrack-python-api 2.3.2)
```python
from ftrack_undo.log import ftrack_session_log_inject
from ftrack_undo.backend.local_disk import FtrackLocalDiskLogBackend
import ftrack_api

# create ftrack session as before
session = ftrack_api.Session()

# inject log, no harm to session object
ftrack_session_log_inject(session, 
                          logging_function=FtrackLocalDiskLogBackend().log)

# use ftrack session as before!
task = session.query('Task').first()
...
```

> proxy design pattern is used here, for more details, please check [wrapt](https://wrapt.readthedocs.io/en/latest/) package.