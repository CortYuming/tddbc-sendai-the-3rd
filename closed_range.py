#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-

class ClosedRange:
    def __init__(self, lower_endpoint, upper_endpoint):
        self.lower_endpoint = lower_endpoint
        self.upper_endpoint = upper_endpoint

    def get_lower_endpoint(self):
        return self.lower_endpoint

    def get_upper_endpoint(self):
        return self.upper_endpoint