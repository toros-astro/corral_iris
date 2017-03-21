#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-03-20T23:42:31.211216 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""irispl tests

"""


# =============================================================================
# IMPORTS
# =============================================================================

from corral import qa

from . import models, steps


# =============================================================================
# LOADER
# =============================================================================

class MyTestCase(qa.TestCase):

    subject = steps.StatisticsCreator

    def setup(self):
        name = models.Name(name="foo")
        self.save(name)

    def validate(self):
        self.assertStreamHas(
            models.Name, models.Name.name=="foo")
        self.assertStreamCount(1, models.Name)

        name = self.session.query(models.Name).first()

        self.assertStreamHas(
            models.Statistics, models.Statistics.name_id==name.id)
        self.assertStreamCount(1, models.Statistics)
