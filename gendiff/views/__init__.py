from gendiff.views.json_view import format as json # noqa F401
from gendiff.views.plain_view import format as plain # noqa F401
from gendiff.views.default_view import format as default # noqa F401


FORMATTERS = (DEFAULT, PLAIN, JSON) = ('default', 'plain', 'json')
