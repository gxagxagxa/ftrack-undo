import logging


class FtrackStreamLogBackend(object):
    __logger_name__ = 'FtrackStreamLogBackend'

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__ + '.' + self.__class__.__name__)

    def log(self, data, *args, **kwargs):
        self.logger.info(data, *args)
