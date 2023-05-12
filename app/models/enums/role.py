from enum import Enum


class Role(str, Enum):
    ADMIN = 'admin'
    Customer = 'customer'
    AGENT = 'agent'
