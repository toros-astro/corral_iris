#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-03-20T23:42:31.211216 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""irispl alerts

"""


# =============================================================================
# IMPORTS
# =============================================================================

from corral import run
from corral.run import endpoints as ep

from . import models


# =============================================================================
# ALERTS
# =============================================================================

class StatisticsAlert(run.Alert):

    model = models.Statistics
    conditions = []
    alert_to = [ep.File("statistics.log")]

    def render_alert(self, utcnow, endpoint, obj):
        return """
            ALERT@{now}: {name}
                - mean_sepal_length = {mean_sepal_length}
                - mean_sepal_width  = {mean_sepal_width}
                - mean_petal_length = {mean_petal_length}
                - mean_petal_width  = {mean_petal_width}
            -------------------------------------------------------
        """.rstrip().format(
            now=utcnow, name=obj.name.name,
            mean_sepal_length=obj.mean_sepal_length,
            mean_sepal_width=obj.mean_sepal_width,
            mean_petal_length=obj.mean_petal_length,
            mean_petal_width=obj.mean_petal_width)


