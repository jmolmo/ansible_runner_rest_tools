#!/usr/bin/env python

import sys

from settings import login

# Log in the server
ar_client = login()

# Create a Group
response = ar_client.http_get("api/v1/groups")

print response.text
