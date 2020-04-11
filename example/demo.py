from vue_i18n_generate.core import update_messages

PATHS = [
  'src'
]

LOCALES = [
  'en_US', 'ru'
]

update_messages(locales=LOCALES, paths=PATHS, i18n_folder='lang')
