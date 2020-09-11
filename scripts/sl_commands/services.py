from . import utils
from . import docker


class Service:
    terminal = '/bin/bash'
    path = None

    @classmethod
    def name(cls):
        return cls.__name__.lower()

    def setup(self):
        raise NotImplementedError('Service does not have a setup step')

    def build(self):
        cmd = f'docker-compose build {self.name()}'
        utils.call_root(cmd)

    def serve(self):
        docker.run(self.name(), './serve.sh')

    def shell(self):
        docker.run(self.name(), self.terminal)


class Banana(Service):

    path = '~/code/recruiter/platform/banana'


class Redis(Service):

    def serve(self):
        cmd = f'docker-compose up {self.name()}'
        utils.call_root(cmd)


_services = [
    Banana,
    Redis
]

_service_dict = {service.name(): service for service in _services}


def get_service(service):
    return _service_dict[service]()
