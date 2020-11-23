import sys

def my_car_game():
    command = ""
    started = False
    print("Welcome to my car game :)")
    print("""
Type any of the following commands:

start - to start the car
stop - to stop the car
honk - to sound the horn
quit - to quit
            """)
    while True:
        command = input("> ").lower()
        if command == "start":
            if started:
                print("Car is already started!!!")
            else:
                started = True
                print("Car started...")
        elif command == "stop":
            if not started:
                print("Car is already stopped!!!")
            else:
                started = False
                print("Car stopped.")
        elif command == "help":
            print("""
    start - to start the car
    stop - to stop the car
    honk- to sound the horn
    quit - to quit
            """)
        elif command == "honk":
            for honk in ["Honk!","Honk Honk!", "HONK HONK!"]:
                print(honk)
        elif command == "quit":
            break
        else:
            print("Sorry, I don't understand that")
    else:
        print("Stop Playing.. There is a bug in the system")

    return


my_car_game()


