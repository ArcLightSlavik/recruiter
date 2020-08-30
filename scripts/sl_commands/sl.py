import argh

from . import services


def setup():
    print('setup command')


def build(service):
    services.get_service(service).build()


def serve():
    print('serve command')


def shell():
    print('shell command')


def stop():
    print('stop command')


def push():
    print('push command')


def deploy():
    print('deploy command')


def execute():
    argh.dispatch_commands([
        setup,
        build,
        serve,
        shell,
        stop,
        push,
        deploy,
    ])
