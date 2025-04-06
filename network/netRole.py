'''
@file netRole.py

@brief file with the netRole enum class
'''
from enum import Enum


class NetRole(Enum):
    '''
    @brief enum class with player role for connection
    '''
    NONE = 0
    HOST = 1
    GUEST =2