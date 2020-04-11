import os

__all__ = ('EMPTY_TERM', 'PATHS', 'LOCALES', 'DESTINATION')

env_src = os.environ.get('VUE_I18N_SRC')
env_locales = os.environ.get('VUE_I18N_LOCALES')

if env_src:
    PATHS = [env_src.split(',')]
else:
    PATHS = [
        'components', 'layouts', 'views', 'mixins', 'pages', 'plugins', 'store'
    ]

if env_src:
    LOCALES = [env_locales.split(',')]
else:
    LOCALES = ['en']

EMPTY_TERM = os.environ.get('VUE_I18N_EMPTY_TERM', "need to fill")
DESTINATION = os.environ.get('VUE_I18N_DESTINATION', "locales")
