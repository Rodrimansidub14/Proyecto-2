Neo4j Products
==============

The jar files in this directory are plugin products. They are compatible with this version of Neo4j, and supported by Neo4j under the terms of your support contract.


Graph Data Science
------------------

Unlocking the Enterprise Edition of the Neo4j Graph Data Science library requires a valid license key. To register for a license, please contact Neo4j at https://neo4j.com/contact-us/?ref=graph-analytics

# GDS documentation https://neo4j.com/docs/graph-data-science/current/installation/


Bloom
-----

Unlocking Bloom for Neo4j requires a valid license key. To register for a license, please contact Neo4j at https://neo4j.com/contact-us/?ref=bloom

# Bloom documentation https://neo4j.com/docs/bloom-user-guide/current/bloom-installation/#bloom-installation


Neo4j Ops Manager
-----------------

# Neo4j Ops Manager documentation https://neo4j.com/docs/ops-manager/current

Enabling Plugins
----------------

To enable these plugins, move the jar files to the plugins directory.
The DBMS needs to be restarted for the jar to be activated.

To enable the products you will need to add the following line(s) in $NEO4J_HOME/conf/neo4j.conf:


# neo4j.conf config to enable GDS

* dbms.security.procedures.unrestricted=gds.*
* dbms.security.procedures.allowlist=gds.*
* gds.enterprise.license_file=/path/to/my/license/keyfile


# neo4j.conf config to enable Bloom

* dbms.security.procedures.unrestricted=bloom.*
* dbms.bloom.license_file=/path/to/my/license/keyfile


# neo4j.conf config to enable both GDS and Bloom

* dbms.security.procedures.unrestricted=gds.*,bloom.*
* dbms.security.procedures.allowlist=gds.*
* gds.enterprise.license_file=/path/to/my/license/keyfile
* dbms.bloom.license_file=/path/to/my/license/keyfile
