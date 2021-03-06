#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-

# 下端点と上端点を与えて閉区間を生成しよう
# 閉区間から下端点と上端点を取得しよう
# 閉区間から文字列表記を取得しよう

from pytest import fail, mark
from closed_range import ClosedRange


@mark.parametrize("lower_endpoint, upper_endpoint", [
    (3, 8),
    (-5, 9),
    (-5, -1),
    (5, 5),
])
def test_create_range(lower_endpoint, upper_endpoint):
    range_interval = ClosedRange(lower_endpoint, upper_endpoint)
    assert range_interval.get_lower_endpoint() == lower_endpoint
    assert range_interval.get_upper_endpoint() == upper_endpoint


def test_convert_able_to_string():
    range_interval = ClosedRange(3, 8)
    assert range_interval.toString() == "[3,8]"


def test_throw_except_initial():
    try:
        ClosedRange(8, 3)
    except RuntimeError:
        return

    fail("not throwing")


def test_contains_between_lower_to_upper():
    range_interval = ClosedRange(3, 8)
    assert range_interval.is_contains(5) is True
    assert range_interval.is_contains(-1) is False


def test_equals_other_closed_range():
    closed_range1 = ClosedRange(3, 8)
    assert closed_range1 == ClosedRange(3, 8)
    assert closed_range1 != ClosedRange(4, 5)


@mark.parametrize("range_a, range_b, actual", [
    ([3, 8], [1, 6], True),
    ([3, 8], [8, 15], True),
    ([3, 8], [9, 12], False),
])
def test_connected_to_other_closed_range(range_a, range_b, actual):
    closed_range1 = ClosedRange(*range_a)
    closed_range2 = ClosedRange(*range_b)
    assert closed_range1.is_connected_to(closed_range2) is actual
