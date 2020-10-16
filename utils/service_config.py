import os


def is_production():
    return _get_environment() == 'prod'


def is_stage():
    return _get_environment() == 'stage'


def get_version():
    return os.environ.get('SL_VERSION')


def get_version_short():
    version = get_version()
    image = version.split('/')[-1]
    return image


def get_info():
    return {'version': get_version(), 'environment': _get_environment()}


def _get_environment():
    return os.environ.get('SL_ENVIRONMENT')
