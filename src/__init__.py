"""FigMan - A Python Configuration Management Library

This package provides tools for managing configuration settings in Python applications.
It supports hierarchical configuration groups, type validation, and serialization
to various formats including JSON and YAML.

The main interface is provided through the FigMan class, which manages the lifecycle
of configuration objects and provides access to configuration groups.

Example:
    >>> from src import FigMan
    >>> config = FigMan()
    >>> settings = config.configuration('app_settings')
    >>> settings('database_url', 'postgresql://localhost:5432/mydb')
    >>> config.save(settings, 'config.json')
"""

from src.figman import FigMan
from src.setting import Setting
from src.group import SubGroup, MasterGroup


__all__ = ['FigMan', 'Setting', 'SubGroup', 'MasterGroup']