#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-

class ClosedRange:
    def __init__(self, lower_endpoint, upper_endpoint):
        if lower_endpoint > upper_endpoint:
            raise

        self.lower_endpoint = lower_endpoint
        self.upper_endpoint = upper_endpoint

    def get_lower_endpoint(self):
        return self.lower_endpoint

    def get_upper_endpoint(self):
        return self.upper_endpoint

    def toString(self):
        return "[{lower},{upper}]".format(lower=self.lower_endpoint,
                                          upper=self.upper_endpoint)
