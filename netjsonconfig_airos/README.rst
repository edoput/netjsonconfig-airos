===================
netjsonconfig-airos
===================

The implementation of the AirOS backend is splitted in many
separate modules belonging to the same package.

The main module is `airos.py` and in there you can find the
the glue that makes it possible to use this package as a plugin
for netjsonconfig.

Every *backend* binds together a JSON schema to validate the
NetJSON input, a list of converters that will convert the NetJSON
input to an intermediate tree data structure and a renderer that
will output this data structure in the format required by the AirOS
firmware.

All the other modules in this directory are of support to the
converters, implementing most of the logic behind certain
configurations values.

Look around for more implementation details but the core logic
is as this.

The backend exposes the validation and rendering of either
NetJSON or native configuration.

Every converter implements a `to_intermediate` method that
will read values from the input NetJSON and return an intermediate
represenation suitable for outputting the native configuration format.

The renderer then takes care of rendering every output from the
converters to the native configuration syntax.

aaa
---

This module abstract the values required to configure a wireless
interface in access point or station mode.

ebtables
--------

This module abstract the values required to configure the `ebtables`
section of an interface.
