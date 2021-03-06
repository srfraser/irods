# Release Notes

## 4.1.7

Release Date: 2015-11-18

### Bug Fixes

 - Fix for irods-grid --hosts option [#2765]

 - Fixes for memory management [#2928] [#2929] [#2942] [#2954]

 - Fixes for compound resource behavior [#2930] [#2939] [#2941]

 - Fix for iphymv targeting child resource [#2933]

 - Fix for python2.6 compatibility [#2940]

 - Refactoring of development libraries [#2945] [#2959]

 - Fix for documentation [#2947]

 - Fix for connection failure messages [#2948]

 - Release of Oracle database plugin for Ubuntu [#2949]

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A4.1.7)

## 4.1.6

Release Date: 2015-10-01

### Bug Fixes

 - Fix for startupPack [#2862]

 - Fix for resource server upgrade [#2863]

 - Fix for inconsistent runtime library links [#2867]

 - Fixes for impostor plugin development use cases [#2868] [#2876]

 - Documentation regarding default ports [#2870]

 - Fix for submodules in source tarball [#2871]

 - Fix for pre-built Debian external packages [#2873]

 - Fix for atomic metadata on empty files [#2875]

 - Fix for int overflow [#2880] [#2881]

 - Fix for recovery from failed installation [#2883]

 - Fix for replication resource voting mechanism [#2884]

 - Fixes for federated remote() microservice call [#2888] [#2903] [#2904]

 - Documentation for delay() and remote() microservices [#2901]

 - Documentation for msiPhyPathReg [#2906]

 - Fixes for edge cases related to rsDataObjClose [#2907] [#2908] [#2909]

 - Fix for hierarchy voting during replication [#2910]

 - Fix for better exception handling [#2914]

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A4.1.6)

## 4.1.5

Release Date: 2015-09-02

### Bug Fixes

 - Fixes for fuse [#2830] [#2837] [#2856]

 - Fixes for SQL statement table holding onto failed queries [#2833] [#2843]

 - Finalize CentOS 7 support [#2834] [#2845] [#2853]

 - Fix for PAM passwords [#2835]

 - Fix for invalid key-value string error [#2836]

 - Fix for bulk iput [#2841]

 - Fix for iticket generation [#2854]

 - Fix for rsDataObjOpen [#2855]

 - Fixes for startupPack [#2857] [#2860]

 - Fix for metadata permissions across Zones [#2858]

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A4.1.5)

## 4.1.4

Release Date: 2015-08-05

### Bug Fixes

 - Fixes for fuse [#2401] [#2509] [#2783]

 - Fix for imeta addw bind variable problem [#2682]

 - Fix shared memory and mutex file cleanup [#2751] [#2752]

 - Fix for perl warning [#2760]

 - Use single quotes for safety/readability [#2764]

 - Fix for using fuser (not available on MacOSX) - replace with lsof [#2772] [#2775] [#2794]

 - Fix irsync recursion [#2779]

 - Fix run-in-place detection [#2781] [#2784]

 - Fix unitialized values [#2782] [#2788]

 - Fix memory allocation mismatch [#2785]

 - Fix for passthru resource using read=0.0 [#2789]

 - Fix for irods-grid when environment properties are missing [#2792]

 - Fix for extra NULL character written by msiDataObjWrite [#2795]

 - Fix for get_db_schema_version.py stderr [#2799]

 - Fix irods_setup.pl detection [#2800]

 - Fix irsync checksums [#2802] [#2810]

 - Fix for ireg with --exclude-path option [#2804]

 - Fix control plane shutdown on resource server [#2807]

 - Add openssl development package dependency [#2808]

 - Add file:// URIs to schema validation [#2811]

 - Fix for cross zone icp/iput as different users [#2813]

 - Fixes for iphymv [#2815] [#2820] [#2821]

 - Fix for isysmeta output alignment [#2819]

 - Fix for data objects in the root dir (/) [#2823]

 - Fix for custom control plane key and port during setup [#2824]

 - Fix for checksum calculations on MacOSX [#2826]

 - Fix for iget parallel transfer [#2828]

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A4.1.4)

## 4.1.3

Release Date: 2015-06-18

### Bug Fixes

  - Fix upgrading with obfuscated password [#2749]

  - Fix imeta query comparison bug [#2748]

  - Fix for cleaning up temporary files during installation [#2745]

  - Run-in-Place installations

    - Fix preflight checks [#2744]

    - Fix for stopping server and killing processes [#2746]

    - Fix for finding database binary tool [#2747]

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A4.1.3)

## 4.1.2

Release Date: 2015-06-05

### Bug Fixes

  - Fix information leakage in izonereport [#2732]

  - Fix misuse of uid for gid in configuration conversion script [#2733] [#2734]

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A4.1.2)

## 4.1.1

Release Date: 2015-06-02

### Bug Fixes

  - Hardening of upgrade process against bad input [#2725] [#2727]

  - Fix for incomplete development package [#2724]

  - Fix for removing package-manager-marked config files [#2723]

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A4.1.1)

## 4.1.0

Release Date: 2015-05-29

### Notable Features

  - Configuration Management - All configuration files are now JSON and schema-backed.

    - Validated Configuration - JSON files are validated against repository of versioned schemas during server startup.

    - Reduced Magic Numbers - Some previously hard coded settings have been moved to server_config.json

    - Integrated izonereport - Produce validated JSON about every server in the Zone.  Useful for debugging and for deployment.

  - Control Plane - New functionality for determining status and grid-wide actions for pause, resume, and graceful shutdown.

  - Weighted Passthru Resource Plugin - A passthru resource can now manipulate its child resource's votes on read and write.

  - Atomic iput with metadata and ACLs - Add metadata and ACLs as soon as data is at rest and registered

  - Key/Value passthru to resource plugins - Can influence resource behavior via user-provided parameters

  - A client hints API to get server configuration information for better user-facing messages

  - Allow only TLS 1.1 and 1.2

  - Dynamic PEP result can halt operation on failure, providing better policy flow control

  - Unified documentation - Markdown-based and automatically generated by MkDocs, hosted at [https://docs.irods.org](https://docs.irods.org)

  - Continuous Testing

    - Automated Ansible-driven python topology suite, including SSL

    - Federation with 3.3.1, 4.0.3, and 4.1.0

    - Well-defined C API for developers

### Notable Bug Fixes

  - Coverity Clean - Fixed over 1100 identified bugs related to memory management, error checking, dead code, and other miscellany.

  - Many permission inconsistencies ironed out

  - Parallel transfer works in multi-homed networked situations, had been resolving IP too early

  - irsync sending only updated files

  - Zip files available via ibun

  - Zero-length file behavior is consistent

  - Delayed rules running correctly

  - Removed built-in PostgreSQL DB Vacuum functionality

  - Removed boot user from install script

  - Removed "run_server_as_root" option

  - Removed roles for storageadmin, domainadmin, and rodscurators

  - Removed obfuscation (SIDKey and DBKey)

### Other Issues

  - [Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A4.1.0)


## 4.0.3

Release Date: 2014-08-20

More flexible installation options (service account name/group), block storage operation fix, impostor resource, memory leak fixes, and security fixes.

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A4.0.3)

## 4.0.2

Release Date: 2014-06-17

Random and RoundRobin resource plugin fix, memory leak fixes, microservice fixes, security fixes, large collection recursive operations, and better server-server authentication setup.

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A4.0.2)

## 4.0.1

Release Date: 2014-06-05

Memory leak fixes, security fixes, --run-in-place, MacOSX support, schema update mechanism.

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A4.0.1)

## 4.0.0

Release Date: 2014-03-28

This is the fourth major release of iRODS and the first merged open source release from RENCI.

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A4.0.0)

## 4.0.0rc2

Release Date: 2014-03-25

This is the second release candidate of the merged open source release from RENCI.  It includes support for MySQL and Oracle databases, GSI, Kerberos, NetCDF, and direct access resources.

## 4.0.0rc1

Release Date: 2014-03-08

This is the first release candidate of the merged open source release from RENCI.  It includes support for MySQL and Oracle databases, NetCDF, and direct access resources.

## 4.0.0b2

Release Date: 2014-02-18

This is the second beta of the merged open source release from RENCI.  It includes pluggable API support and external S3 and WOS resource plugin packages.

## 4.0.0b1

Release Date: 2014-01-17

This is the first beta of the merged open source release from RENCI.  It includes pluggable database support and separate packages for the standalone server and its plugins.

## 3.0.1

Release Date: 2013-11-16

This is the second open source release from RENCI. It includes Federation compliance with Community iRODS and signaling for dynamic post-PEPs to know whether their operation failed.

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A3.0.1)

## 3.0.1rc1

Release Date: 2013-11-14

This is the first release candidate of the second open source release from RENCI.  It includes a new "--tree" view for `ilsresc` and a more powerful `irodsctl stop`.  In addition, package managers should now be able to handle upgrades more gracefully.

## 3.0.1b2

Release Date: 2013-11-12

This is the second beta of the second open source release from RENCI.  It includes certification work with the Jargon library, more CI testing, and minor fixes.

## 3.0.1b1

Release Date: 2013-10-31

This is the first beta of the second open source release from RENCI. It includes pluggable network and authentication support as well as a rebalance option and migration support for the composable resources.

## 3.0

Release Date: 2013-06-05

This is the first open source release from RENCI. It includes all the features mentioned below and has been both manually and continuously tested.

[Full GitHub Listing](https://github.com/irods/irods/issues?q=milestone%3A3.0)

## 3.0rc1

Release Date: 2013-05-14

This is the first release candidate from RENCI.  It includes PAM support, additional resources (compound, universalMSS, replication, random, and nonblocking), and additional documentation.

## 3.0b3

Release Date: 2013-03-15

This is the third release from RENCI.  It includes a new package for CentOS 6+, support for composable resources, and additional documentation.

## 3.0b2

Release Date: 2012-06-25

This is the second release from RENCI.  It includes packages for iCAT, Resource, iCommands, and development, in both DEB and RPM formats. Also includes more documentation.

## 3.0b1

Release Date: 2012-03-01

This is the first release from RENCI, based on the iRODS 3.0 community codebase.

