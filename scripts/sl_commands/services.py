from . import utils
from . import docker


class Service:
    terminal = '/bin/bash'
    path = None

    @classmethod
    def name(cls):
        return cls.__name__.lower()

    def build(self):
        cmd = f'docker-compose build {self.name()}'
        utils.call_root(cmd)

    def serve(self):
        cmd = f'docker-compose up {self.name()}'
        utils.call_root(cmd)

    def shell(self):
        docker.run(self.name(), self.terminal)

    def stop(self):
        utils.call_root(f'docker-compose stop {self.name()}')
        utils.call_root(f'docker rm {docker.list_exited()}')


class Dev(Service):

    path = '/app/recruiter'


class Banana(Service):

    path = '/app/recruiter/platform/banana'


class Pypi(Service):
    pass


class Redis(Service):
    pass


class Postgres(Service):
    pass


_services = [
    Dev,
    Banana,
    Pypi,
    Redis,
    Postgres,
]

_service_dict = {service.name(): service for service in _services}


def get_service(service):
    return _service_dict[service]()
