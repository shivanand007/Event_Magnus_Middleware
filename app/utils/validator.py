'''

This file contains all validator funcations

For this file to work, It is Strongly recommended to run this code as administrator

'''
import subprocess
import socket

'''' Internal Imports '''
from app.utils import logger


def is_ip_reachable(ip_address, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Set a timeout for the connection attempt

        # Attempt to connect to the IP address and port
        result = sock.connect_ex((ip_address, port))

        # Check if the connection was successful (0 indicates success)
        if result == 0:
            logger.info("handshake success Ip is Reachable")
        return result == 0
    except socket.error:
        logger.error("handshake failed, server ip not Reachable")
        return False






