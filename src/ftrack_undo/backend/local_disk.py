import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional

from ftrack_undo.backend.constant import FtrackLogEnum, LOG_FORMATTER


class FtrackLocalDiskLogBackend(object):
    __logger_name__ = 'FtrackLocalDiskLogBackend'

    def __init__(self, filename: Optional[str] = None) -> None:
        self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)
        self.log_filename = self._get_log_filename(filename)
        handler = RotatingFileHandler(self.log_filename, maxBytes=16 * 1024 * 1024)
        handler.setFormatter(LOG_FORMATTER)
        self.logger.addHandler(handler)

    def _get_log_filename(self, filename: Optional[str] = None):
        filename = filename or os.environ.get(FtrackLogEnum.FTRACK_LOCAL_DISK_LOG_FILENAME.value, '')
        if filename:
            if not Path(filename).parent.exists():
                Path(filename).parent.mkdir(parents=True, exist_ok=True)
            return filename
        else:
            import tempfile
            return tempfile.NamedTemporaryFile()

    def log(self, data, *args, **kwargs):
        self.logger.info('{}, {}, {}'.format(data, args, kwargs))
