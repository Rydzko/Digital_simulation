from user import User


class Network:

    # possible number of supported users in system
    user_counter = 10
    user = 0

    def __init__(self):
        self.buffer = []
        self.queue = []
        self.users_list = []
        self.users_queue_list = []
        self.no_users = 0

    def initialize(self):
        self.buffer = []
        self.queue = []
        self.users_list = []
        self.users_queue_list = []
        self.no_users = 0

    def generate_packet(self):
        global user
        print(self.users_list)
        self.no_users += 1
        if self.user_counter > len(self.users_list):
            self.buffer.append(User(self.no_users))
            self.users_list.append(self.no_users)
            print(self.users_list)
            user = self.no_users
        else:
            self.users_queue_list.append(self.no_users)
            print('After add user to queue:')
            print(self.users_queue_list)
        # Use number of users as user ID
        return user
