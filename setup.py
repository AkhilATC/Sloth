from setuptools import setup,find_packages

setup(
    name='sloth',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'bottle',
        'MarkupSafe',
        'Click',
        'gevent',
        'Eel',
        'Jinja2',
        'art',
    ],
    entry_points={
        'console_scripts': [
            'sloth = sloth_func.sloth_cli:get_sloth',
        ],
    },
)
