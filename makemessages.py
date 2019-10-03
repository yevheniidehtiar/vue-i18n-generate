from config import *

import os
import re
import collections
import six
import json
import logging

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


def list_to_object(l):
    tree_dict = EMPTY_TERM  # empty term
    for key in reversed(l):
        tree_dict = {key: tree_dict}
    return tree_dict


def str_to_object(val):
    keys = val.split('.')
    return list_to_object(keys)


def generate_messages():
    messages = []
    for folder in PATHS:
        for file in os.listdir(folder):
            file_path = '%s/%s' % (folder, file)
            if os.path.isfile(file_path):
                data = file_read(file_path)
                if data:
                    messages += mining_terms(data)
            elif os.path.isdir(file_path):
                for sub_file in os.listdir(file_path):
                    subfile_path = '%s/%s' % (file_path, sub_file)
                    if os.path.isfile(subfile_path):
                        messages += mining_terms(file_read(subfile_path))

    terms = {}
    for message in messages:
        deep_dict_update(terms, str_to_object(message))

    return terms


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


def mining_terms(text):
    regex = re.compile(r'\Wtc?\([\"\'][\w\.]+[\"\']\)')
    matches = regex.findall(text)
    return [re.search(r'[\"\'].+[\"\']', match).group()[1:-1] for match in matches]


def update_messages():
    print("...Start generation new i18n terms files")
    for locale in LOCALES:
        path = f'lang/{locale}.js'
        old_messages = {}
        if os.path.isfile(path):
            data = file_read(path)
            if data:
                try:
                    #  15 is shift to skip `export default`
                    old_messages = json.loads(data[15:])
                    logger.debug(f'...Updating {locale}.js')
                except Exception as e:
                    logger.error(f'...Read error {locale}.js')
                    logger.error(f'...Creating {locale}.js')
                    raise ChildProcessError
        else:
            print(f'...Creating {locale}.js')

        new_messages = generate_messages()
        deep_dict_update(new_messages, old_messages)

        messages_dump = json.dumps(new_messages, ensure_ascii=False, indent=2)
        try:
            with open(path, 'w') as f:
                f.write("export default ")
                f.write(messages_dump)
                if len(old_messages.keys()) > 0:
                    print(f'...Updated {locale}.js')
                else:
                    print(f'...Created {locale}.js')
        except Exception as e:
            logger.error(f'...Error on saving {path}')


update_messages()
