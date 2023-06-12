from user import User


class Network:

    # possible number of supported users in system
    user_counter = 3
    user = 0

    def __init__(self):
        self.buffer = []
        self.queue = []
        self.users_list = []
        self.users_queue_list = []
        # self.temp_list = []
        self.no_users = 0

    def initialize(self):
        self.buffer = []
        self.queue = []
        self.users_list = []
        self.users_queue_list = []
        self.no_users = 0

    def generate_packet(self):
        global user
        # print('SYSTEM1')
        print(self.users_list)
        self.no_users += 1
        # print('SYSTEM2')
        if self.user_counter >= len(self.users_list):
            self.buffer.append(User(self.no_users))
            self.users_list.append(self.no_users)
            print(self.users_list)
            user = self.no_users
        else:
            self.users_queue_list.append(self.no_users)
            print('After add user to queue:')
            print(self.users_queue_list)
        if len(self.users_queue_list) != 0 and self.user_counter >= len(self.users_list):
            self.users_list.append(self.users_queue_list[0])
            user = self.users_queue_list[0]
            self.users_queue_list.pop(0)
            print('After delete user with queue:')
            print(self.users_queue_list)
        # Use number of users as user ID
        return user
