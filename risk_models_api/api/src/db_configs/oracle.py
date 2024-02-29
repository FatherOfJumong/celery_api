from dataclasses import dataclass

import os


@dataclass(init=False)
class Oracle:
    """Configuration class for oracle databases"""
    user = os.getenv('ORACLE_USER')
    password = os.getenv('ORACLE_PASSWORD')
    name = os.getenv('ORACLE_DATABASE')
    ip = os.getenv('ORACLE_IP')
    port = os.getenv('ORACLE_PORT')
    uri = "oracle+cx_oracle://%s:%s@%s:%s/%s" % (user, password, ip, port, name)

