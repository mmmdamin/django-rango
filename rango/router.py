from django.db.utils import DEFAULT_DB_ALIAS

from rango import current_db


class MultiHostDBRouter(object):
    """
    The multiple database router.
    """

    def db_for_read(self, model, **hints):
        return getattr(current_db, 'db', DEFAULT_DB_ALIAS) or DEFAULT_DB_ALIAS

    db_for_write = db_for_read
