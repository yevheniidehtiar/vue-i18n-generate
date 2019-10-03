# About
Nuxt and vue project i18n don't have cli to grab from code all i18n messages like:
`$t('msg'), $t('msg.nested.like.object.json'), $tc("verbose", {param1: 'value'})`

This utility parse your source codebase and save all found terms for each locale to `lang/${locale}.js`.

Updating strategy: "Your original terms will save over generated" and manually added terms to files will be saved after each generating.

## How to use
Play and learn with `example`. Run `demo_generate` to watch the magic ^-) 


## Cookbook
Add `core.py, nuxt_config.py, nuxt_generate.py` to the root of your project source code.

Created and used the utility is on Nuxt, but you can reconfigure it for your project.   
Edit `nuxt_config.py` to reconfigure. Run `nuxt_generate.py`

````
PATHS = [
  'project', 'folders', 'that', 'you', 'want', 'to', 'parse',
]

LOCALES = [
  'en_US', 'संस्कृतम्', 'saṃskṛtam'
]
````
 

## Requirements 
Python 2/3. Tested on 3.7.

I hope that everyone coder have python in working env. But for "zero-pythonists"
 
`pip install -r requirements.txt` 

 There is only `six` package. 

## TODO:
1. ✅ Add support to messages with params like `$t('msg', {param1: 'value'})` 
2. Add cli parameters for Vue and Nuxt unique logic (project folders)


## Contributing

Here is main regex to parse files: 
https://regex101.com/r/Ramwl1/4

You can fork and improve this
