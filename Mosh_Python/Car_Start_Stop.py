command = ""
started = False
while True:
    command = input(">").lower()
    if command =="start" :
        if started:
            print("car is already started")
        else:
            started = True
            print("Car is started")
    elif command == "stop" :
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car is stopped")
    elif command == "help" :
        print("""
              start - Start the car
              stop - Stop the car
              help - Display this help message
              quit - Exit the program""")
    elif command == "quit" :
        break