from __future__ import print_function
import ckan.plugins as p
from . import db
import logging


from ckan import model
import click

log = logging.getLogger(__name__)

def get_commands():
    return [featured]

@click.group()
def featured():
    """Features resource views.
    """
    pass

@featured.command()
def initdb():
    """Creates the necessary tables in the database.
    """
    if not db.featured_table.exists():
        db.featured_table.create()
        log.info('Featured Views table created')
    else:
        log.warning('Features Views table already exists')
        print ('Featured Views table already exists')


