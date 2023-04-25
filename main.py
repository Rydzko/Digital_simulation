from main_loop import MainLoop

# protect users from accidentally invoking the script
if __name__ == "__main__":
    print('Started Simulation')
    main_loop = MainLoop()
    main_loop.run(100)
