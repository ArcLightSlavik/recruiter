import argh

from . import services


def build(service):
    services.get_service(service).build()


def serve(service):
    services.get_service(service).serve()


def shell(service):
    services.get_service(service).shell()


def stop(service):
    services.get_service(service).stop()


def pip_build(service):
    services.get_service(service).pip_build()


def pip_publish(service):
    services.get_service(service).pip_publish()


def push():
    print('push command')


def deploy():
    print('deploy command')


def execute():
    argh.dispatch_commands([
        build,
        serve,
        shell,
        stop,
        pip_build,
        pip_publish,
        push,
        deploy,
    ])
