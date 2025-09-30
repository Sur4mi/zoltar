import time


def start():
    coin = input("INSERT COIN: Y/N  ").lower()
    if coin == "y":
        print("Your tribute has been taken...")
        time.sleep(2)
        print("The price is paid...")
        time.sleep(2)
        print("The future is now yours to fear.")
        time.sleep(2)
    else:
        print("Mysteries remain locked to those who refuse the price...")
        time.sleep(2)
        print("What is denied now will haunt you later.")
        time.sleep(2)
        start() 

start()