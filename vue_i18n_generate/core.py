"""
  Thanks to https://stackoverflow.com/questions/3232943/update-value-of-a-nested-dictionary-of-varying-depth
            https://stackoverflow.com/questions/40401886/how-to-create-a-nested-dictionary-from-a-list-in-python
            https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory

  Regex:
            https://regex101.com/r/Ramwl1/1

"""

import os
import re
import collections
import six
import json
import logging
import copy

logger = logging.Logger(__name__)

# python 3.8+ compatibility
try:
    collectionsAbc = collections.abc
except:
    collectionsAbc = collections


def deep_dict_update(d, u):
    for k, v in six.iteritems(u):
        dv = d.get(k, {})
        if not isinstance(dv, collectionsAbc.Mapping):
            d[k] = v
        elif isinstance(v, collectionsAbc.Mapping):
            d[k] = deep_dict_update(dv, v)
        else:
            d[k] = v
    return d


def str_to_object(string, empty_term='need to fill'):
    keys = string.split('.')
    tree_dict = empty_term  # empty term
    for key in reversed(keys):
        tree_dict = {key: tree_dict}
    return tree_dict


def generate_messages(paths):
    messages = []

    for folder in paths:
        messages += mine_folder(folder)

    terms = {}
    for message in messages:
        deep_dict_update(terms, str_to_object(message))

    return terms


def abspath(r, c):
    path = os.path.abspath(os.path.join(r, c))
    resource = 'Folder' if os.path.isdir(path) else 'file'
    if os.path.isdir(path):
        print('\n')
    print(f'...Scan {resource} `{os.path.relpath(path)}`')
    return path


def mine_folder(folder):
    messages = []
    for root, subs, files in os.walk(folder):
        for sub in subs:
            messages += mine_folder(abspath(root, sub))
        messages += mine_files(root, files)
    return messages


def mine_files(root, files):
    messages = []
    for file in files:
        messages += mine_terms(file_read(abspath(root, file)))
    return messages


def file_read(path):
    try:
        file_handle = open(path, "r")
        if file_handle.mode == "r":
            content = file_handle.read()
            file_handle.close()
            return content
    except Exception as e:
        return None
    return None


def mine_terms(text):
    regex = re.compile(r'\Wtc?\([\"\'][\w\.]+[\"\'][,)]')
    matches = regex.findall(text)
    return [re.search(r'[\"\'].+[\"\']', match).group()[1:-1] for match in matches]


def update_messages(locales, paths, i18n_folder='lang', format='js'):
    print("...Start generation new i18n terms files")
    generated_messages = generate_messages(paths)

    if format not in ('js', 'json'):
        raise ValueError('format should be `js` or `json`')

    for locale in locales:
        path = f'{i18n_folder}/{locale}.{format}'
        old_messages = {}
        new_messages = copy.deepcopy(generated_messages)

        if os.path.isfile(path):
            data = file_read(path)
            if data:
                try:
                    #  15 is shift to skip `export default`
                    old_messages = json.loads(data[15:] if format == 'js'
                                              else data)
                    logger.debug(f'...Updating {locale}.js')

                    deep_dict_update(new_messages, old_messages)
                except Exception as e:
                    logger.error(f'...Read error {locale}.js')
                    logger.error(f'...Creating {locale}.js')
                    raise ChildProcessError
        else:
            print(f'...Creating {locale}.js')

        messages_dump = json.dumps(new_messages, ensure_ascii=False, indent=2)

        try:
            with open(path, 'w') as f:
                if format == 'js':
                    f.write("export default ")
                f.write(messages_dump)
                if len(old_messages.keys()) > 0:
                    print(f'...Updated {locale}.js')
                else:
                    print(f'...Created {locale}.js')
        except Exception as e:
            logger.error(f'...Error on saving {path}')
