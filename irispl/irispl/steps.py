#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-03-20T23:42:31.211216 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""irispl steps

"""


# =============================================================================
# IMPORTS
# =============================================================================

from corral import run

from . import models


# =============================================================================
# STEPS
# =============================================================================

class StatisticsCreator(run.Step):

    model = models.Name
    conditions = []

    def process(self, name):
        stats = self.session.query(models.Statistics).filter(
            models.Statistics.name_id==name.id).first()
        if stats is None:
            yield models.Statistics(
                name_id=name.id,
                mean_sepal_length=0., mean_sepal_width=0.,
                mean_petal_length=0., mean_petal_width=0.,
                min_sepal_length=0., min_sepal_width=0.,
                min_petal_length=0., min_petal_width=0.,
                max_sepal_length=0., max_sepal_width=0.,
                max_petal_length=0., max_petal_width=0.)


class SetosaStatistics(run.Step):

    model = models.Statistics
    conditions = [
        models.Statistics.name.has(name="Iris-setosa"),
        models.Statistics.mean_sepal_length==0.]
    groups = ["default", "statistics"]

    def process(self, stats):
        sepal_length, sepal_width, petal_length, petal_width = [], [], [], []
        for obs in stats.name.observations:
            sepal_length.append(obs.sepal_length)
            sepal_width.append(obs.sepal_width)
            petal_length.append(obs.petal_length)
            petal_width.append(obs.petal_width)

        stats.mean_sepal_length = sum(sepal_length) / len(sepal_length)
        stats.mean_sepal_width = sum(sepal_width) / len(sepal_width)
        stats.mean_petal_length = sum(petal_length) / len(petal_length)
        stats.mean_petal_width = sum(petal_width) / len(petal_width)

        stats.min_sepal_length = min(sepal_length)
        stats.min_sepal_width = min(sepal_width)
        stats.min_petal_length = min(petal_length)
        stats.min_petal_width = min(petal_width)

        stats.max_sepal_length = max(sepal_length)
        stats.max_sepal_width = max(sepal_width)
        stats.max_petal_length = max(petal_length)
        stats.max_petal_width = max(petal_width)


class VersicolorStatistics(run.Step):

    model = models.Statistics
    conditions = [
        models.Statistics.name.has(name="Iris-versicolor"),
        models.Statistics.mean_sepal_length==0.]
    groups = ["default", "statistics"]

    def process(self, stats):
        sepal_length, sepal_width, petal_length, petal_width = [], [], [], []
        for obs in stats.name.observations:
            sepal_length.append(obs.sepal_length)
            sepal_width.append(obs.sepal_width)
            petal_length.append(obs.petal_length)
            petal_width.append(obs.petal_width)

        stats.mean_sepal_length = sum(sepal_length) / len(sepal_length)
        stats.mean_sepal_width = sum(sepal_width) / len(sepal_width)
        stats.mean_petal_length = sum(petal_length) / len(petal_length)
        stats.mean_petal_width = sum(petal_width) / len(petal_width)

        stats.min_sepal_length = min(sepal_length)
        stats.min_sepal_width = min(sepal_width)
        stats.min_petal_length = min(petal_length)
        stats.min_petal_width = min(petal_width)

        stats.max_sepal_length = max(sepal_length)
        stats.max_sepal_width = max(sepal_width)
        stats.max_petal_length = max(petal_length)
        stats.max_petal_width = max(petal_width)


class VirginicaStatistics(run.Step):

    model = models.Statistics
    conditions = [
        models.Statistics.name.has(name="Iris-virginica"),
        models.Statistics.mean_sepal_length==0.]
    groups = ["default", "statistics"]

    def process(self, stats):
        sepal_length, sepal_width, petal_length, petal_width = [], [], [], []
        for obs in stats.name.observations:
            sepal_length.append(obs.sepal_length)
            sepal_width.append(obs.sepal_width)
            petal_length.append(obs.petal_length)
            petal_width.append(obs.petal_width)

        stats.mean_sepal_length = sum(sepal_length) / len(sepal_length)
        stats.mean_sepal_width = sum(sepal_width) / len(sepal_width)
        stats.mean_petal_length = sum(petal_length) / len(petal_length)
        stats.mean_petal_width = sum(petal_width) / len(petal_width)

        stats.min_sepal_length = min(sepal_length)
        stats.min_sepal_width = min(sepal_width)
        stats.min_petal_length = min(petal_length)
        stats.min_petal_width = min(petal_width)

        stats.max_sepal_length = max(sepal_length)
        stats.max_sepal_width = max(sepal_width)
        stats.max_petal_length = max(petal_length)
        stats.max_petal_width = max(petal_width)
