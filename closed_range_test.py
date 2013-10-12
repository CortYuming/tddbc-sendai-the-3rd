#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-

# 下端点と上端点を与えて閉区間を生成しよう
# 閉区間から下端点と上端点を取得しよう
# 閉区間から文字列表記を取得しよう

from pytest import fail
from closed_range import ClosedRange



def test_create_range():
    range_interval = ClosedRange(3, 8)
    assert range_interval.get_lower_endpoint() == 3
    assert range_interval.get_upper_endpoint() == 8
    assert range_interval.toString() == "[3,8]"

def test_throw_except_initiral():
    ClosedRange(8, 3)
    # try:
    #     ClosedRange(8, 3)
    #     fail("not throwing")
    # except:
    #     pass
