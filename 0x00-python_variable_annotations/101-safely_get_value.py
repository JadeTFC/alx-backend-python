#!/usr/bin/env python3
""" safely_get_value """
from typing import Mapping, Union, Any, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Gets a value with a key if it exists. """
    if key in dct:
        return dct[key]
    else:
        return default
