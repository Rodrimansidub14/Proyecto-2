@ECHO OFF
rem Copyright (c) "Neo4j"
rem Neo4j Sweden AB [http://neo4j.com]
rem This file is a commercial add-on to Neo4j Enterprise Edition.

SETLOCAL

Powershell -NoProfile -NonInteractive -NoLogo -ExecutionPolicy Bypass -File "%~dp0neo4j-admin.ps1" %*
EXIT /B %ERRORLEVEL%
