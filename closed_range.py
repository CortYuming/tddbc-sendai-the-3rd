#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-

class ClosedRange:
    def __init__(self, lower_endpoint, upper_endpoint):
        if lower_endpoint > upper_endpoint:
            raise RuntimeError('lower endpoint is more than upper endpoint')

        self.lower_endpoint = lower_endpoint
        self.upper_endpoint = upper_endpoint

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
