from rango.utils import get_host


def make_key(key, key_prefix, version):
    return ':'.join([key_prefix, str(version), get_host(default=''), key])
