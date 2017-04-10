#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-03-20T23:42:31.211216 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""Global configuration for irispl

"""


# =============================================================================
# IMPORTS
# =============================================================================

import logging
import os


# =============================================================================
# CONFIGURATIONS
# =============================================================================

#: Path where the settings.py lives
PATH = os.path.abspath(os.path.dirname(__file__))

#: Run the steps and alerts with the debug number of processes
DEBUG_PROCESS = True

#: Sets the threshold for this logger to lvl. Logging messages which are less
#: severe than lvl will be ignored
LOG_LEVEL = logging.INFO

#: Template of string representation of every log of irispl format
#: see: https://docs.python.org/2/library/logging.html#logrecord-attributes
LOG_FORMAT = (
        "[irispl-%(name)s-%(levelname)s@%(asctime)-15s] %(message)s")


PIPELINE_SETUP = "irispl.pipeline.Pipeline"


#: Database connection string formated ad the URL is an RFC-1738-style string.
#: See: http://docs.sqlalchemy.org/en/latest/core/engines.html
CONNECTION = "sqlite:///irispl-dev.db"


# Loader class
LOADER = "irispl.load.Loader"


# Pipeline processor steps
STEPS = [
    "irispl.steps.StatisticsCreator",
    "irispl.steps.SetosaStatistics",
    "irispl.steps.VirginicaStatistics",
    "irispl.steps.VersicolorStatistics"]


# The alerts
ALERTS = ["irispl.alerts.StatisticsAlert"]

# This values are autoimported when you open the shell
SHELL_LOCALS = {}


# SMTP server configuration
EMAIL = {
    "server": "",
    "tls": True,
    "user": "",
    "password": ""
}

MIGRATIONS_SETTINGS = os.path.join(PATH, "migrations", "alembic.ini")

PATH = os.path.abspath(os.path.dirname(__file__))
IRIS_PATH = os.path.join(PATH, "iris.csv")
