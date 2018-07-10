===================
netjsonconfig-airos
===================

.. warning:

    This module will eat your socks! If you like your socks eaten in a different
    manner add an issue.

The ``AirOs`` backend allows to generate AirOS v8.3 compatible configurations.


.. toctree::

    intermediate
    airos-upgrade

Converters with defaults
------------------------

`NetJSON <http://netjson.org>`_ does not map explicitly to various section of the AirOS device configuration.
For those section we have provided default values that should work both in ``bridge``
and ``router`` mode.

The list of "defaulted" converters follows:

* Discovery
* Dhcpc

  * ``dhcpc.devname`` defaults to ``br0``

* Dyndns
* Httpd
* Igmpproxy
* Iptables

  * ``iptables.sys.mgmt.devname`` defaults to ``br0``

* Netconf

  * the first interface with a ``gateway`` specified is the management interface in ``bridge`` mode
  * the first interface with a ``gateway`` specified is the ``wan`` interface in ``router`` mode

* Pwdog
* Radio

  * most of the configuration for the radio interface is taken from a PowerBeam ``PBE-5AC-400``

* Syslog
* System
* Telnetd
* Tshaper
* Unms
* Update
* Upnpd

General settings
----------------

From the ``general`` property we can configure the contact and the location for
a device using the ``contact`` and ``location`` properties.

The following snippet specify both contact and location:

.. code-block:: json

    {
        "type": "DeviceConfiguration",
        "general": {
            "contact": "user@example.com",
            "location": "Up on the roof"
        }
    }

Network interface
-----------------

From the ``interfaces`` key we can configure the device network interfaces.

AirOS supports the following types of interfaces

* **network interfaces**: may be of type ``ethernet``
* **wirelesss interfaces**: must be of type ``wireless``
* **bridge interfaces**: must be of type ``bridge``

A network interface can be designed to be the management interfaces by setting
the ``role`` key to ``mlan`` on the address chosen.

As an example here is a snippet that set the vlan ``eth0.2`` to be the
management interface on the address ``192.168.1.20``

.. code-block:: json

   {
       "interfaces": [
           {
               "name": "eth0.2",
               "type": "ethernet",
               "addresses": [
                   {
                       "address": "192.168.1.20",
                       "family": "ipv4",
                       "role": "mlan",
                       "mask": 24,
                       "proto": "static"
                   }
               ]
           }
       ]
   }

Ethernet
^^^^^^^^

The ``ethernet`` interface can be configured to allow auto-negotiation and flow
control with the properties ``autoneg`` and ``flowcontrol``

As an example here is a snippet that enables both auto-negotiation and flow control

.. code-block:: json

    {
        "interfaces": [
            {
                "type": "ethernet",
                "name": "eth0",
                "autoneg": true,
                "flowcontrol": true
           }
       ]
   }

Role
^^^^

Interfaces can be assigned a ``role`` to mimic the web interfaces features.

As an example setting the ``role`` property of an address to ``mlan`` will add
the role ``mlan`` to the interface configuration and set it as the management interface.

.. warning::

    Not setting a management interface will lock you out from the web interface

Here is the snippet to set the role to ``mlan``

.. code-block:: json

    {
        "interfaces": [
            {
                "type": "ethernet",
                "name": "eth0",
                "addresses": [
                    {
                        "family": "ipv4",
                        "proto": "static",
                        "address": "192.168.1.1",
                        "role": "mlan"
                    }
                ]
            }
        ]
    }


This is the list of roles available for a device in ``bridge`` mode:

* ``mlan`` for the management interface

This is the list of roles available for a device in ``router`` mode:

* ``wan`` for the wan interface
* ``lan`` for the lan interface


GUI
---

As an extension to `NetJSON <http://netjson.org/rfc.html>`_ you can use the
``gui`` key to set the language of the interface 

The default values for this key are reported below

.. code-block:: json

    {
        "type": "DeviceConfiguration",
        "gui": {
            "language": "en_US",
        }
    }

Netmode
-------

AirOS v8.3 can operate in ``bridge`` and ``router`` mode (but defaults to
``bridge``) and this can be specified with the ``netmode`` property.

.. code-block:: json

    {
        "type": "DeviceConfiguration",
        "netmode": "bridge"
    }

NTP servers
-----------

This is an extension to the `NetJSON <http://netjson.org/rfc.html>`_ specification.

By setting the key ``ntp`` property in your input you can provide the
configuration for the ntp client running on the device.

.. code-block:: json

    {
        "type": "DeviceConfiguration",
        "ntp": {
            "enabled": true,
            "server": [
                "0.ubnt.pool.ntp.org"
            ]
        }
    }

For the lazy one we provide these defaults

.. code-block:: json

    {
        "type": "DeviceConfiguration",
        "ntp": {
            "enabled": true,
            "server": [
                "0.pool.ntp.org",
                "1.pool.ntp.org",
                "2.pool.ntp.org",
                "3.pool.ntp.org"
            ]
        }
    }

Radio
-----

The following properties of a ``Radio Object`` are used during the conversion,
the others have been set to safe defaults.

* ``name``

Ssh
---

We can specify the configuration for the ssh server on the antenna using the
``sshd`` property.

This snippet shows how to configure the ssh server with the default values.

.. code-block:: json

    {
        "type": "DeviceConfiguration",
        "sshd": {
            "port": 22,
            "enabled": true,
            "password_auth": true
        }
    }

And this shows how to set the authorized ssh public keys

.. code-block:: json

    {
        "type": "DeviceConfiguration",
        "sshd": {
            "keys": [
                {
                    "type": "ssh-rsa",
                    "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBEEhdDJIbHVHIXQQ8dzH3pfmIbZjlrcIV+YkZM//ezQtINTUbqolCXFsETVVwbCH6d8Pi1v1lCDgILbkOOivTIKUgG8/84yI4VLCH03CAd55IG7IFZe9e6ThT4/MryH8zXKGAq5rnQSW90ashZaOEH0wNTOhkZmQ/QhduJcarevH4iZPrq5eM/ClCXzkF0I/EWN89xKRrjMB09WmuYOT48n5Es08iJxwQ1gKfjk84Fy+hwMKVtOssfBGuYMBWByJwuvW5xCH3H6eVr1GhkBRrlTy6KAkc9kfAsSpkHIyeb/jAS2hr6kAh6cxapKENHxoAdJNvMEpdU11v6PMoOtIb edoput@hypnotoad",
                    "comment": "my shh key",
                    "enabled": true
                }
            ]
        }
    }

Users
-----

We can specify the user password as a blob divided into ``salt`` and ``hash``.

From the antenna configuration take the user section.

.. code-block:: ini

    users.status=enabled
    users.1.status=enabled
    users.1.name=ubnt
    users.1.password=$1$yRo1tmtC$EcdoRX.JnD4VaEYgghgWg1

In the line ``users.1.password=$1$yRo1tmtC$EcdoRX.JnD4VaEYgghgWg1`` there are
both the salt and the password hash in the format ``$ algorithm $ salt $ hash``,
e.g in the previous block ``algorithm=1``, ``salt=yRo1tmtC`` and
``hash=EcdoRX.JnD4VaEYgghgWg1``.

To specify the password in NetJSON use the ``user`` property.

.. code-block:: json

    {
        "type": "DeviceConfiguration",
        "user": {
            "name": "ubnt",
            "passsword": "EcdoRX.JnD4VaEYgghgWg1",
            "salt": "yRo1tmtC"
        }
    }


WPA2
----

AirOS v8.3 supports both WPA2 personal (PSK+CCMP) and WPA2 enterprise (EAP+CCMP)
as an authentication protocol. The only ciphers available is CCMP.

As an antenna only has one wireless network available only the first wireless
interface will be used during the generation.

As an example here is a snippet that set the authentication protocol to WPA2 personal

.. code-block:: json

    {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "wireless": {
                    "mode": "station",
                    "radio": "ath0",
                    "ssid": "ap-ssid-example",
                    "encryption": {
                        "protocol": "wpa2_personal",
                        "key": "changeme"
                    }
                }
            }
        ]
    }

And another that set the authentication protocol to WPA2 enterprise

.. code-block:: json

    {
        "interfaces": [
            {
                "name": "wlan0",
                "type": "wireless",
                "wireless": {
                    "mode": "station",
                    "radio": "ath0",
                    "ssid": "ap-ssid-example",
                    "encryption": {
                        "protocol": "wpa2_enterprise",
                        "identity": "my-identity",
                        "password": "changeme",
                    }
                }
            }
        ]
    
