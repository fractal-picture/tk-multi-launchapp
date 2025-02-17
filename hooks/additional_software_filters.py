#!/bin/env python
# -*- coding: utf-8 -*-
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk

HookBaseClass = sgtk.get_hook_baseclass()


class AdditionalSoftwareFilters(HookBaseClass):

    def get_additional_filters(self):
        """Hook to add additional filters the Software entity query"""
        return []
