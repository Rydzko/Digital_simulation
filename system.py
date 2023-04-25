from user import User


class Network:

    def __init__(self):
        self.buffer = []
        self.no_users = 0

    def initialize(self):
        self.buffer = []
        self.no_users = 0

    def generate_packet(self):
        self.no_users += 1
        self.buffer.append(User(self.no_users))

        # Use number of users as user ID
        return self.no_users
