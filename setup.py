from setuptools import setup, find_packages

setup(
    name="ESMFigMan",
    version="0.1.0",
    author="Donald Reilly",
    author_email="donald.reilly.jr@outlook.com",
    description="Manages configuration files",
    long_description=open("README.md").read(),
    url="https://github.com/donald-reilly/ESMFigMan",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "PyYaml>=6.0.2"
    ]
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requries="3.13"
)