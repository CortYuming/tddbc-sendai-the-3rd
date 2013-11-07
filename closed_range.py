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
        return number in range(self.lower_endpoint, last_point)

    def is_connected_to(self, other_crosed_range):
        start_last_point = self.upper_endpoint + 1
        start_closed_range = range(self.lower_endpoint,
                                   start_last_point)

        stop_last_point = other_crosed_range.get_upper_endpoint() + 1
        stop_closed_range = range(other_crosed_range.get_lower_endpoint(),
                                  stop_last_point)

        if len(set(start_closed_range).intersection(stop_closed_range)):
            return True
        return False
