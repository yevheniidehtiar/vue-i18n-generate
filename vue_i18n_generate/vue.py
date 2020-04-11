from vue_config import *
from vue_i18n_generate.core import update_messages

update_messages(locales=LOCALES, paths=PATHS, i18n_folder='locales')
