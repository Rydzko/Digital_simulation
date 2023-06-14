from main_loop import MainLoop
from base_station import Generator
from generateuserevent import GenerateUserEvent
from reportevent import ReportEvent
from matplotlib import pyplot as plt

# protect users from accidentally invoking the script
if __name__ == "__main__":
    print('Started Simulation')
    print('******************')

    x = int(input("How many users should the system support?\n"))
    main_loop = MainLoop()
    # number of users served in entire system
    main_loop.run(x)
    # print(Generator.users_served)
    # print(GenerateUserEvent.users_in_system)
    # if len(Generator.users_served) < len(GenerateUserEvent.users_in_system):
    #    difference = len(GenerateUserEvent.users_in_system) - len(Generator.users_served)
    #    for i in range(0, difference):
    #        Generator.users_served.append(Generator.users_served[-1])
    # plt.plot(GenerateUserEvent.users_in_system, Generator.users_served)
    # plt.title("Initial phase length")
    # plt.xlabel("Users served")
    # plt.ylabel("Users in system")
    # plt.show()

    print("Average number of user switches between stations:")
    print(ReportEvent.HO_counter/x)
    print("Average number of dropped radio connections:")
    print(ReportEvent.counter/x)