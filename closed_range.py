#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-

class ClosedRange:
    def __init__(self, lower_endpoint, upper_endpoint):
        if lower_endpoint > upper_endpoint:
            raise RuntimeError('lower endpoint is more than upper endpoint')

        self.lower_endpoint = lower_endpoint
        self.upper_endpoint = upper_endpoint

    def __eq__(self, other):
        is_equal_lower_endpoint = self.lower_endpoint == other.get_lower_endpoint()
        is_equal_upper_endpoint = self.upper_endpoint == other.get_upper_endpoint()
        return is_equal_lower_endpoint and is_equal_upper_endpoint

    def __ne__(self, other):
        is_equal_lower_endpoint = self.lower_endpoint != other.get_lower_endpoint()
        is_equal_upper_endpoint = self.upper_endpoint != other.get_upper_endpoint()
        return is_equal_lower_endpoint and is_equal_upper_endpoint


    def get_lower_endpoint(self):
        return self.lower_endpoint

    def get_upper_endpoint(self):
        return self.upper_endpoint

    def toString(self):
        return "[{lower},{upper}]".format(lower=self.lower_endpoint,
                                          upper=self.upper_endpoint)

    def is_contains(self, number):
        last_point = self.upper_endpoint + 1
        return number in [n for n in range(self.lower_endpoint, last_point) if n > 0]

        # for num in range(self.lower_endpoint, last_point):
        #     if num == number:
        #         return True
        # return False

    def is_conected_to(self, other):
        closed_range1 = range(self.lower_endpoint, self.upper_endpoint + 1)
        closed_range2 = range(other.get_lower_endpoint(), other.get_upper_endpoint() + 1)

        for num in closed_range1:
            if num in closed_range2:
                return True
        return False
