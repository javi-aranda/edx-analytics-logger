from setuptools import setup

with open('requirements/requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='edx-analytics-logger',
    version='1.1.4',
    packages=['edx_analytics_logger'],
    url='https://github.com/javi-aranda/edx-analytics-logger',
    license='MIT',
    author='javisenberg',
    description='edx powered ApiBackend',
    long_description=open('README.rst').read(),
    install_requires=install_requires,
)
