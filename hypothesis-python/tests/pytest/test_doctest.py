# coding=utf-8
#
# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis/
#
# Most of this work is copyright (C) 2013-2019 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://mozilla.org/MPL/2.0/.
#
# END HEADER

from __future__ import absolute_import, division, print_function

pytest_plugins = "pytester"

func_with_doctest = """
def hi():
    '''
    >>> i = 5
    >>> i-1
    4
    '''
"""


def test_can_run_doctests(testdir):
    script = testdir.makepyfile(func_with_doctest)
    result = testdir.runpytest(script, "--doctest-modules")
    assert result.ret == 0
