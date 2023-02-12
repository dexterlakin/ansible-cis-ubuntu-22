# 1.1.1.3 Ensure mounting of udf filesystems is disabled (Automated)

## Profile Applicability

Level 2 - Server
Level 2 - Workstation

## Description

The udf filesystem type is the universal disk format used to implement ISO/IEC 13346 and ECMA-167 specifications. This is an open vendor filesystem type for data storage on a broad range of media. This filesystem type is necessary to support writing DVDs and newer optical disc formats.

## Rationale

Removing support for unneeded filesystem types reduces the local attack surface of the system. If this filesystem type is not needed, disable it.

## Impact

Microsoft Azure requires the usage of udf .
`udf` should not be disabled on systems run on Microsoft Azure.
