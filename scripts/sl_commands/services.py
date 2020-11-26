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


class PipService(Service):

    def pip_build(self):
        docker.run(Dev.name(), f'cd {self.path} && ./build.sh')

    def pip_publish(self):
        docker.run(Dev.name(), f'cd {self.path} && ./publish.sh')


class Dev(Service):

    path = '/home/recruiter'


class Banana(Service):

    path = '/home/recruiter/platform/banana'


class Utils(PipService):

    path = '/home/recruiter/pipable/utils'

    def serve(self):
        raise NotImplementedError


class Pypi(Service):
    pass


class Redis(Service):
    pass


class Postgres(Service):
    pass


_services = [
    Dev,
    Banana,
    Utils,
    Pypi,
    Redis,
    Postgres,
]

_service_dict = {service.name(): service for service in _services}


def get_service(service):
    return _service_dict[service]()
