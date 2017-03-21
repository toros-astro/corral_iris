#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-03-20T23:42:31.211216 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""irispl main loader

"""


# =============================================================================
# IMPORTS
# =============================================================================

import csv

from corral.conf import settings
from corral import run

from irispl import models


# =============================================================================
# LOADER
# =============================================================================

class Loader(run.Loader):

    def setup(self):
        # abrimos el archivo aqui y lo asignamos a una variable de instancia
        self.fp = open(settings.IRIS_PATH)

    def teardown(self, *args):
        # verificamos que el archivo este abierto
        if self.fp and not self.fp.closed:
            self.fp.close()

    def get_name_instance(self, row):
        name = self.session.query(models.Name).filter(
            models.Name.name == row["Name"]).first()

        # if exists we need don't need to create one
        if name is None:
            name = models.Name(name=row["Name"])

            # we need to add the new instance and save it
            self.save(name)
            self.session.commit()

        return name

    def store_observation(self, row, name):
        return models.Observation(
            name=name,
            sepal_length=row["SepalLength"], sepal_width=row["SepalWidth"],
            petal_length=row["PetalLength"], petal_width=row["PetalWidth"])

    def generate(self):
        # ahora usamos "self.fp" para el reader
        for row in csv.DictReader(self.fp):
            name = self.get_name_instance(row)
            obs = self.store_observation(row, name)
            yield obs
