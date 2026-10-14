import os

shutdown = input("Do you want to shutdown the computer? (yes/no): ")
if shutdown.lower() == "no":
    exit()
else:
    os.system("shutdown /s /t 1")