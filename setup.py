from setuptools import find_packages
from setuptools import setup


setup(
    name="project",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
