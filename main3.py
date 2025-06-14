import os
import platform

def shutdown():
    choice = input("Do you want to shutdown the system? (Yes/No): ")

    if choice.lower() == "yes":
        system = platform.system()
        print("Shutting down the system...")
        if system == "Windows":
            os.system("shutdown /s /t 1")
        elif system == "Linux" or system == "Darwin":
            os.system("shutdown now")
        else:
            print("Unsupported operating system.")
    elif choice.lower() == "no":
        print("Shutdown cancelled.")
    else:
        print("Sorry, I didn’t understand your input.")

# Call the function
shutdown()
