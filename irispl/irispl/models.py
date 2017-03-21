#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-03-20T23:42:31.211216 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""irispl database models

"""

# =============================================================================
# IMPORTS
# =============================================================================

from corral import db


# =============================================================================
# MODELS (Put your models below)
# =============================================================================

class Name(db.Model):

    __tablename__ = 'Name'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)


class Observation(db.Model):

    __tablename__ = 'Observation'

    id = db.Column(db.Integer, primary_key=True)

    name_id = db.Column(
        db.Integer, db.ForeignKey('Name.id'), nullable=False)
    name = db.relationship("Name", backref=db.backref("observations"))

    sepal_length = db.Column(db.Float, nullable=False)
    sepal_width = db.Column(db.Float, nullable=False)
    petal_length = db.Column(db.Float, nullable=False)
    petal_width = db.Column(db.Float, nullable=False)


class Statistics(db.Model):

    __tablename__ = 'Statistics'

    id = db.Column(db.Integer, primary_key=True)

    name_id = db.Column(
        db.Integer, db.ForeignKey('Name.id'), nullable=False, unique=True)
    name = db.relationship(
        "Name", backref=db.backref("statistics"), uselist=False)

    mean_sepal_length = db.Column(db.Float, nullable=False)
    mean_sepal_width = db.Column(db.Float, nullable=False)
    mean_petal_length = db.Column(db.Float, nullable=False)
    mean_petal_width = db.Column(db.Float, nullable=False)

    min_sepal_length = db.Column(db.Float, nullable=False)
    min_sepal_width = db.Column(db.Float, nullable=False)
    min_petal_length = db.Column(db.Float, nullable=False)
    min_petal_width = db.Column(db.Float, nullable=False)

    max_sepal_length = db.Column(db.Float, nullable=False)
    max_sepal_width = db.Column(db.Float, nullable=False)
    max_petal_length = db.Column(db.Float, nullable=False)
    max_petal_width = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return "<Statistics of '{}'>".format(self.name.name)
