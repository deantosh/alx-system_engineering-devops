# Project Overview

HTTP is not a secure communication protocol. If a person is able to tap into the communication
channel, all the data being sent between the client and the server is easily read.

This challenge brings about a security threat, especially when sensitive information i.e bank details
is being transferred.

To deal with this challenge a more secure communication protocol is used between the end points.
This secure protocol is HTTP SSL. The secure protocol encrypts/decrypts the data being shared between
the client and the server.

HTTPS SSL advantages:
1. Creating a more secure client-server connection.
2. Implementing HAproxy SSL termination.
3. Config HAproxy to redirect http traffic to https.
