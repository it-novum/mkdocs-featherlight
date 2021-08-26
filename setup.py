from setuptools import setup

setup(
    name='featherlight',
    version='1.0.0',
    author='it-novum',
    author_email='community@openitcockpit.io',
    description='Markdown extension for MkDocs to wrap images in featherlight',
    py_modules=['featherlight'],
    install_requires = ['markdown>=2.5'],
    license='MIT License',
)
