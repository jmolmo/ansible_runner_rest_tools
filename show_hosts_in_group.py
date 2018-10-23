#!/usr/bin/env python

import sys

from settings import login

if len(sys.argv)< 2:
    print("A group name must be provided")
    sys.exit(2)

group_name = sys.argv[1]

if not group_name:
    print("A group name must be provided")
    sys.exit(2)

# Log in the server
ar_client = login()

# Create a Host
response = ar_client.http_get("api/v1/groups/%s" % group_name)

print response.text
