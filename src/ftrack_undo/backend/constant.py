import logging
from enum import Enum


class FtrackLogEnum(Enum):
    FTRACK_LOCAL_DISK_LOG_FILENAME = 'FTRACK_LOCAL_DISK_LOG_FILENAME'
    FTRACK_DATABASE_LOG_URL = 'FTRACK_DATABASE_LOG_URL'


LOG_FORMATTER = logging.Formatter('%(levelname)s\t'
                                  '%(asctime)s\t'
                                  '%(name)s\t'
                                  '%(message)s')
