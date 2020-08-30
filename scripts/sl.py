import argh


def setup():
    print('setup command')


def build():
    print('build command')


def serve():
    print('serve command')


def stop():
    print('stop command')


def push():
    print('push command')


def shell():
    print('shell command')


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
