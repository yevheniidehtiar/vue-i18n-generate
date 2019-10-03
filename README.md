# About
Nuxt and vue project i18n don't have cli to grab from code all i18n messages like:
`$t('msg'), $t('msg.nested'), $tc('verbose')`

This utility parse your source codebase and save all found terms for each locale to `lang/${locale}.js`.

Updating strategy: "Your original terms will save over generated" and manually added terms to files will be saved after each generating.


## Cookbook
Add `makemessages.py` to the root of your project source code.

Created and used the utility is on Nuxt, but you can reconfigure it for your project.   
Edit the `config.py` 

````
EMPTY_TERM = "you can define your own"

PATHS = [
  'project', 'folders', 'that', 'you', 'want', 'to', 'parse',
]

LOCALES = [
  'en_US', 'संस्कृतम्', 'saṃskṛtam'
]
````
 

## Requirements 
Python 2/3. Tested on 3.7.


## TODO:
1. Add support to messages with params like `$t('msg', {param1: 'value'})`
2. Add cli parameters for Vue and Nuxt unique logic
