"""Write a set of Python classes that can simulate an Internet application in which one party, Alice, is periodically creating a set of packets that she wants to send to Bob. An Internet process is continually checking if Alice has any packets to send, and if so, it delivers them to Bob’s computer, and Bob is periodically checking if his computer has a packet from Alice, and, if so, he reads and deletes it."""

import random
import threading
import socket


class Alice:
    """Alice Class

    Periodically creates a set of packets to be sent to Bob"""

    def __init__(self):
        pass


class Bob:
    """Bob Class

    Periodically checks for any new messages"""

    def __init__(self):
        pass


class InternetProcess:
    """Internet Process

    Continually checks if Alice has any messages to send"""

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("127.0.0.1", 2077))
        self.stop = False

    def receive(self):
        client, address = self.server.accept()
        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024)

        if nickname == "BOB":
            bobclient = client

        elif nickname == "ALICE":
            aliceclient = client
