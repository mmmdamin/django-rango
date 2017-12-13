from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='django-rango',
    version='0.0.3',
    description='A database router based on incoming host address.',
    long_description=readme,
    author='Amin Sabbaghian',
    author_email='mmmdamin@gmail.com',
    url='https://github.com/mmmdamin/django-rango',
    license='MIT',
    packages=find_packages()
)
