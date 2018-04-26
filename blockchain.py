import hashlib
import json
from time import time

from proof_of_work import proof_of_work, valid_proof


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a block

        :param block: <dict> block
        :return: <str>
        """

    @property
    def last_block(self):
        """
        Returns the last block in the chain
        """
        pass
