========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/tc/badges/kolla.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html

.. Change things from this point on

==============
Kolla Overview
==============

The Kolla project is a member of the OpenStack `Big Tent
Governance <https://governance.openstack.org/tc/reference/projects/index.html>`__.

Kolla's mission statement is:

::

    To provide production-ready containers and deployment tools for operating
    OpenStack clouds.

Kolla provides `Docker <https://docker.com/>`__ containers,
`Ansible <https://ansible.com/>`__ playbooks to deploy OpenStack on baremetal
or virtual machine to meet Kolla's mission.

Kolla has out of the box defaults for a working basic deployment, and also
implements complete customization. This model permits operators with minimal
experience to deploy OpenStack quickly and as the operator's experience grows
modify the OpenStack configuration to suit the operator's exact requirements.

Getting Started
===============

Learn about Kolla by reading the documentation online
`Kolla <https://docs.openstack.org/kolla/latest/>`__.

Get started by reading the `Kolla Ansible Developer
Quickstart <https://docs.openstack.org/kolla-ansible/latest/user/quickstart.html>`__.

The Kolla Repository
====================

The Kolla repository is one of three deliverables of the OpenStack Kolla
project. The three deliverables that make up the Kolla project are:

================   =========================================================
Deliverable        Repository
================   =========================================================
kolla              https://git.openstack.org/cgit/openstack/kolla
kolla-ansible      https://git.openstack.org/cgit/openstack/kolla-ansible
kolla-cli          https://git.openstack.org/cgit/openstack/kolla-cli
================   =========================================================

The `Docker images <https://docs.docker.com/engine/userguide/storagedriver/
imagesandcontainers/>`__
are built by the Kolla project maintainers. A detailed process for
contributing to the images can be found in the `image building
guide <https://docs.openstack.org/kolla/latest/admin/image-building.html>`__.

The Kolla developers build images in the `kolla` namespace for every tagged
release.

You can view the available images on `Docker Hub
<https://hub.docker.com/u/kolla/>`__ or with the Docker CLI::

    $ sudo docker search kolla

OpenStack services
------------------

Kolla provides images to deploy the following OpenStack projects:

- `Almanach <https://almanach.readthedocs.io/>`__
- `Aodh <https://docs.openstack.org/aodh/latest/>`__
- `Barbican <https://docs.openstack.org/barbican/latest/>`__
- `Bifrost <https://docs.openstack.org/bifrost/latest/>`__
- `Blazar <https://docs.openstack.org/blazar/latest/>`__
- `Ceilometer <https://docs.openstack.org/ceilometer/latest/>`__
- `Cinder <https://docs.openstack.org/cinder/latest/>`__
- `CloudKitty <https://docs.openstack.org/cloudkitty/latest/>`__
- `Congress <https://docs.openstack.org/congress/latest/>`__
- `Designate <https://docs.openstack.org/designate/latest/>`__
- `Dragonflow <https://docs.openstack.org/dragonflow/latest/>`__
- `EC2-API <https://wiki.openstack.org/wiki/EC2API>`__
- `Freezer <https://docs.openstack.org/freezer/latest/>`__
- `Glance <https://docs.openstack.org/glance/latest/>`__
- `Heat <https://docs.openstack.org/heat/latest/>`__
- `Horizon <https://docs.openstack.org/horizon/latest/>`__
- `Ironic <https://docs.openstack.org/ironic/latest/>`__
- `Karbor <https://docs.openstack.org/karbor/latest/>`__
- `Keystone <https://docs.openstack.org/keystone/latest/>`__
- `Kuryr <https://docs.openstack.org/kuryr/latest/>`__
- `Magnum <https://docs.openstack.org/magnum/latest/>`__
- `Manila <https://docs.openstack.org/manila/latest/>`__
- `Mistral <https://docs.openstack.org/mistral/latest/>`__
- `Monasca <https://docs.openstack.org/monasca-api/latest/>`__
- `Murano <https://docs.openstack.org/murano/latest/>`__
- `Neutron <https://docs.openstack.org/neutron/latest/>`__
- `Nova <https://docs.openstack.org/nova/latest/>`__
- `Octavia <https://docs.openstack.org/octavia/latest/>`__
- `Panko <https://docs.openstack.org/panko/latest/>`__
- `Rally <https://docs.openstack.org/rally/latest/>`__
- `Sahara <https://docs.openstack.org/sahara/latest/>`__
- `Searchlight <https://docs.openstack.org/searchlight/latest/>`__
- `Senlin <https://docs.openstack.org/senlin/latest/>`__
- `Solum <https://docs.openstack.org/solum/latest/>`__
- `Swift <https://docs.openstack.org/swift/latest/>`__
- `Tacker <https://docs.openstack.org/tacker/latest/>`__
- `Tempest <https://docs.openstack.org/tempest/latest/>`__
- `Trove <https://docs.openstack.org/trove/latest/>`__
- `Vitrage <https://docs.openstack.org/vitrage/latest/>`__
- `Vmtp <https://vmtp.readthedocs.io/en/latest/>`__
- `Watcher <https://docs.openstack.org/watcher/latest/>`__
- `Zaqar <https://docs.openstack.org/zaqar/latest/>`__
- `Zun <https://docs.openstack.org/zun/latest/>`__

Infrastructure components
-------------------------

Kolla provides images to deploy the following infrastructure components:

- `Ceph <https://ceph.com/>`__ implementation for Cinder, Glance and Nova
- `Certmonger <https://pagure.io/certmonger>`__ a service to simplify interaction
  with CAs on networks which use PKI.
- `Chrony <https://chrony.tuxfamily.org/>`__ a versatile implementation
  of the Network Time Protocol (NTP).
- `Collectd <https://collectd.org>`__,
  `InfluxDB <https://influxdata.com/time-series-platform/influxdb/>`__, and
  `Grafana <https://grafana.org>`__ for performance monitoring.
- `Elasticsearch <https://www.elastic.co/de/products/elasticsearch>`__ and
  `Kibana <https://www.elastic.co/products/kibana>`__ to search, analyze,
  and visualize log messages.
- `Etcd <https://coreos.com/etcd/>`__ a distributed key value store that provides
  a reliable way to store data across a cluster of machines.
- `Fluentd <https://www.fluentd.org/>`__ as an open source data collector
  for unified logging layer.
- `Gnocchi <http://gnocchi.xyz/>`__ A time-series storage database.
- `HAProxy <https://www.haproxy.org/>`__ and
  `Keepalived <http://www.keepalived.org/>`__ for high availability of services
  and their endpoints.
- `Kafka <https://kafka.apache.org/documentation/>`__ A distributed streaming
  platform.
- `MariaDB and Galera Cluster <https://mariadb.com/kb/en/library/galera-cluster/>`__
  for highly available MySQL databases.
- `Memcached <https://www.memcached.org/>`__ a distributed memory object caching system.
- `MongoDB <https://www.mongodb.org/>`__ as a database back end for Panko.
- `Open vSwitch <http://openvswitch.org/>`__ and Linuxbridge back ends for Neutron.
- `Linux ptp <http://linuxptp.sourceforge.net/>`__ an implementation of the Precision
  Time Protocol (PTP) according to IEEE standard 1588 for Linux.
- `Prometheus <https://prometheus.io/>`__ an open-source systems monitoring
  and alerting toolkit originally built at SoundCloud.
- `Qdrouterd <https://qpid.apache.org/components/dispatch-router/index.html>`__ as a
  direct messaging back end for communication between services.
- `RabbitMQ <https://www.rabbitmq.com/>`__ as a broker messaging back end for
  communication between services.
- `Telegraf <https://www.docs.influxdata.com/telegraf/>`__ as a plugin-driven server
  agent for collecting & reporting metrics.
- `ZooKeeper <https://zookeeper.apache.org/>`__ as a centralized service for maintaining
  configuration information, naming, providing distributed synchronization, and providing
  group services.

Directories
===========

-  ``contrib`` - Contains sample template override files.
-  ``doc`` - Contains documentation.
-  ``docker`` - Contains jinja2 templates for the Docker build system.
-  ``etc`` - Contains a reference etc directory structure which requires
   configuration of a small number of configuration variables to build
   docker images.
-  ``tests`` - Contains functional testing tools.
-  ``tools`` - Contains tools for interacting with the kolla repository.
-  ``specs`` - Contains the Kolla communities key arguments about
   architectural shifts in the code base.

Getting Involved
================

Need a feature? Find a bug? Let us know! Contributions are much
appreciated and should follow the standard `Gerrit
workflow <https://docs.openstack.org/infra/manual/developers.html>`__.

-  We communicate using the #openstack-kolla irc channel.
-  File bugs, blueprints, track releases, etc on
   `Launchpad <https://launchpad.net/kolla>`__.
-  Attend weekly
   `meetings <https://wiki.openstack.org/wiki/Meetings/Kolla>`__.
-  Contribute `code <https://git.openstack.org/cgit/openstack/kolla>`__.

Contributors
============

Check out who is `contributing
code <http://stackalytics.com/?module=kolla-group&metric=commits>`__ and
`contributing
reviews <http://stackalytics.com/?module=kolla-group&metric=marks>`__.

Notices
=======

Docker and the Docker logo are trademarks or registered trademarks of
Docker, Inc. in the United States and/or other countries. Docker, Inc.
and other parties may also have trademark rights in other terms used herein.
