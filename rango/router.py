from django.db.utils import DEFAULT_DB_ALIAS

from rango.utils import get_host


class MultiHostDBRouter(object):
    """
    The multiple database router.
    """

    def db_for_read(self, model, **hints):
        return get_host(default=DEFAULT_DB_ALIAS)

    db_for_write = db_for_read
