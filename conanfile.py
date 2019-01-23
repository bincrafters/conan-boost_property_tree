#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostProperty_TreeConan(base.BoostBaseConan):
    name = "boost_property_tree"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_property_tree"
    lib_short_names = ["property_tree"]
    header_only_libs = ["property_tree"]
    b2_requires = [
        "boost_any",
        "boost_assert",
        "boost_bind",
        "boost_config",
        "boost_core",
        "boost_format",
        "boost_iterator",
        "boost_mpl",
        "boost_multi_index",
        "boost_optional",
        "boost_range",
        "boost_serialization",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits"
    ]


