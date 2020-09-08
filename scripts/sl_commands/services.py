from abc import ABC

from . import utils
from . import docker


class Service:
    terminal = '/bin/bash'

    @classmethod
    def name(cls):
        return cls.__name__.lower()

    def setup(self):
        raise NotImplementedError('Service does not have a setup step')

    def build(self):
        cmd = f'docker-compose build {self.name()}'
        utils.call_root(cmd)

    def shell(self):
        docker.run(self.name(), self.terminal, no_deps=True)


class Banana(Service, ABC):

    path = None  # @TODO need to change this later


_services = [
    Banana
]

_service_dict = {service.name(): service for service in _services}


def get_service(service):
    return _service_dict[service]()
