#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-03-20T23:42:31.211216 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""Alembic migrations for irispl

See: http://alembic.readthedocs.org/en/latest/api/runtime.html

"""

# =============================================================================
# IMPORTS
# =============================================================================

from alembic import context

from corral.db import engine, Model


# =============================================================================
# CONFIGURATIONS
# =============================================================================

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
# config = context.config

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


# =============================================================================
# FUNCTIONS
# =============================================================================

def run_migrations():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=Model.metadata)

        with context.begin_transaction():
            context.run_migrations()


# =============================================================================
# RUN
# =============================================================================

run_migrations()
