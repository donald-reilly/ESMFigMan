from setuptools import setup, find_packages

setup(
    name="figman",  
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="Donald Reilly",
    author_email="donald.reilly.jr@outlook.com",
    description="A configuration manager for managing groups and settings.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
)