# Project Overview

Project focusses on implementing the Master-Slave Database Replica infrastructure using MySQL.

This creates a MySQL backup for the database, that can be used incasethe primary database fails.

In this setup the primary database hnadels the write operations while the replicas handle the read operations.
