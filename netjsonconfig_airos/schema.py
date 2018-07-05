import json
import pkg_resources

"""
AirOS specific JSON-Schema definition
"""
from netjsonconfig.schema import schema as default_schema
from netjsonconfig.utils import merge_config

default_ntp_servers = [
        "0.pool.ntp.org",
        "1.pool.ntp.org",
        "2.pool.ntp.org",
        "3.pool.ntp.org"
]


"""
This defines a new property in the ``Interface``.

The management interface is the one that exposes the
web interface

It can be used on a single interface (ethernet, vlan) or
on a bridge
"""

schema_path = pkg_resources.resource_filename(__name__, 'schema/airos.json')

with open(schema_path, 'r') as airos_schema:
    override_schema = json.load(airos_schema)

schema = merge_config(default_schema, override_schema)

schema['definitions']['encryption_wireless_property_ap'] = \
    override_schema['definitions']['encryption_wireless_property_ap']

schema['definitions']['encryption_wireless_property_sta'] = \
    override_schema['definitions']['encryption_wireless_property_sta']
