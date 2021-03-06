#!/usr/bin/env python
from abc import (
    ABCMeta,
    abstractmethod,
)


class Provider(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self, args):
        pass

    @abstractmethod
    def populate_parser(self, parser):
        pass
