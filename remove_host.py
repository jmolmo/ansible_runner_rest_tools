#!/usr/bin/env python

import sys

from settings import login

if len(sys.argv)< 3:
    print("A group name and a host name must be provided")
    sys.exit(2)

group_name = sys.argv[1]
host_name = sys.argv[2]

if not group_name or not host_name:
    print("A group name and a host name must be provided")
    sys.exit(2)

# Log in the server
ar_client = login()

# Create a Host
response = ar_client.http_delete("api/v1/hosts/%s/groups/%s" % (host_name, group_name))

print response.text
