from . import utils


def run(docker_image, cmd, no_deps=True):
    # If zeppelin_{service}_1 is not running, runs a temp container, execute command and remove container.
    # If container is already running, "exec" inside container

    docker_service_name = f'zeppelin_{docker_image}_1'
    if not is_container_running(docker_service_name):
        print(f'<{docker_image}> is not running, so I will start a container for this command and remove it afterwards')
        options = ['--rm']
        if no_deps:
            options.append('--no-deps')
        option_str = ' '.join(options)
        cmd = f'docker-compose run {option_str} {docker_image} bash -c "{cmd}"'
        utils.call_root(cmd)
        print('Cleaning up container')
    else:
        print(f'Service <{docker_image}> is already running, so this command executes there')
        utils.call_root(f'docker-compose exec {docker_image} bash -c "{cmd}"')


def is_container_running(container_name):
    # Is Docker container 'name' currently active?
    res = utils.call_output(f'docker ps -f name={container_name} -q')
    res = res.strip()
    if len(res) > 0:
        return True
    return False


def list_exited():
    res = utils.call_output("docker ps -a --format '{{.Names}}' -f 'status=exited'")
    res_decoded = res.decode('utf-8')
    return res_decoded.strip().split('\n')[0]
