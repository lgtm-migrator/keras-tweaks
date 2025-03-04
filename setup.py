from setuptools import setup
import os


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fp:
        s = fp.read()
    return s


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(name='keras-tweaks',
      version=get_version("keras_tweaks/__init__.py"),
      description='Utility functions for Keras/Tensorflow2.',
      long_description=read('README.rst'),
      url='http://github.com/ulf1/keras-tweaks',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='Apache License 2.0',
      packages=['keras_tweaks'],
      install_requires=[
          'tensorflow>=2,<3',
          'sparsity_pattern>=0.4.4,<1'],
      python_requires='>=3.7',
      zip_safe=True)
