from rango import current_host


def get_host(default=None):
    value = getattr(current_host, 'host', default)
    if not value and default:
        value = default
    return value
