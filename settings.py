import logging
from ansible_runner_svc import Client

SERVER_ADDR = "192.168.121.1"
SERVER_PORT = "5001"
USERNAME = "admin"
PASSWD = "admin"
CERT = ""


def login():

    result = None

    # Logger
    log = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    log.addHandler(handler)

    # Ansible runner service client
    result = Client(server = SERVER_ADDR,
                    port = SERVER_PORT,
                    user = USERNAME,
                    password = PASSWD,
                    certificate = '',
                    logger = log)

    if not result.is_operative():
        print("Ansible Runner Service not available. "
            "Check external server status or connection options. "
            "If configuration options changed try to "
            "disable/enable the module.")

    return result
