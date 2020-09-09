import argh

from . import services


def setup(service):
    services.get_service(service).setup()


def build(service):
    services.get_service(service).build()


def serve(service):
    services.get_service(service).serve()


def shell(service):
    services.get_service(service).shell()


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
