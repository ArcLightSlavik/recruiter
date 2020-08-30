import subprocess


def call(cmd):
    return subprocess.check_call(cmd, shell=True)  # @TODO: avoid using shell=true


def call_root(cmd):
    call(f'cd ~/code/recruiter && {cmd}')
