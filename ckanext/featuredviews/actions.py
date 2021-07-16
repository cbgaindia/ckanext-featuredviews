from . import db
import logging
import ckan.model as model

from ckan.plugins.toolkit import get_validator, ValidationError
from ckan.lib.dictization import table_dictize
from ckan.logic import NotFound

import ckan.lib.navl.dictization_functions as df

log = logging.getLogger(__name__)

schema = {
    'resource_view_id': [get_validator('not_empty'), str],
    'package_id': [get_validator('ignore_empty'), str],
    'canonical': [get_validator('boolean_validator'), str],
    'homepage': [get_validator('boolean_validator'), str]
}

schema_get = {
    'resource_view_id': [get_validator('not_empty'), str]
}

def featured_create(context, data_dict):
    data, errors = df.validate(data_dict, schema, context)

    if errors:
        raise ValidationError(errors)

    featured = db.Featured()
    featured.resource_view_id = data['resource_view_id']
    featured.canonical = data.get('canonical', False)
    featured.homepage = data.get('homepage', False)

    resource_id = model.ResourceView.get(featured.resource_view_id).resource_id
    featured.package_id = model.Package.get(resource_id).package_id

    featured.save()

    session = context['session']
    session.add(featured)
    session.commit()

    return table_dictize(featured, context)

def featured_show(context, data_dict):
    data, errors = df.validate(data_dict, schema_get, context)

    if errors:
        raise ValidationError(errors)

    featured = db.Featured.get(resource_view_id=data['resource_view_id'])
    if featured is None:
        raise NotFound()

    return table_dictize(featured, context)

def featured_upsert(context, data_dict):
    data, errors = df.validate(data_dict, schema, context)

    if errors:
        raise ValidationError(errors)

    featured = db.Featured.get(resource_view_id=data['resource_view_id'])
    if featured is None:
        featured = db.Featured()

    featured.resource_view_id = data['resource_view_id']

    print (data['canonical'])

    if 'canonical' in data:
        featured.canonical = data['canonical'] == 'True'

    if 'homepage' in data:
        featured.homepage = data['homepage'] == 'True'

    resource_id = model.ResourceView.get(featured.resource_view_id).resource_id
    featured.package_id = model.Resource.get(resource_id).package_id

    featured.save()

    session = context['session']
    session.add(featured)
    session.commit()

    return table_dictize(featured, context)
