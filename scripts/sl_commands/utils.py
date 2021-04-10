import os
import shlex
import subprocess


def call(cmd):
    command = shlex.split(cmd)
    return subprocess.check_call(command)


def call_root(cmd):
    os.chdir(os.path.expanduser('~/code/zeppelin'))
    call(f'{cmd}')


def call_output(cmd):
    command = shlex.split(cmd)
    return subprocess.check_output(command)


def get_main_folder():
    if os.path.exists('/app/zeppelin'):
        return '/app/zeppelin'

    user_folder = os.path.expanduser('~/code/zeppelin')
    if os.path.exists(user_folder):
        return user_folder
    raise Exception('Recruiter folder not found')
