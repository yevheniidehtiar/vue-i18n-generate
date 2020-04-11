from setuptools import find_packages, setup

__version__ = "0.1.3"


setup(
    # package name in pypi
    name='vue-i18n-generate',
    # extract version from module.
    version=__version__,
    description="This utility parse your source codebase and save terms to "
                "local files",
    long_description="Nuxt and vue project i18n don't have cli to grab from "
                     "code all i18n messages like: $t('msg'), "
                     "$t('msg.nested.like.object.json'), $tc(\"verbose\", "
                     "{param1: 'value'}). This utility parse your source "
                     "codebase and save all found terms for each locale to "
                     "lang/${locale}.js.\nUpdating strategy: Your original "
                     "terms will save over generated and manually added "
                     "terms to files will be saved after each generating.",
    classifiers=['tool', 'vue', 'i18n'],
    keywords=['vue', 'vue-i18n', 'i18n', 'tool'],
    author='Yevhenii Dehtiar',
    author_email='yevhenii.dehtiar@gmail.com',
    url='https://github.com/yevheniidehtiar/vue-i18n-generate',
    license='',
    # include all packages in the egg, except the test package.
    packages=find_packages(exclude=['example', '*.tests.*']),
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=[
        'six',
    ]
)
