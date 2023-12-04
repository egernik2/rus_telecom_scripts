from time import sleep
from keyboard import send

def main():
    print("Наслаждайся...")
    while True:
        for i in range(10):
            send("numlock")
            sleep(0.1)
            send("capslock")
            sleep(0.1)
            send(70)
            sleep(0.1)
        for i in range(10):
            send("numlock")
            send(70)
            sleep(0.15)
            send("capslock")
            sleep(0.15)
        for i in range(10):
            send(70)
            sleep(0.1)
            send("capslock")
            sleep(0.1)
            send("numlock")
            sleep(0.1)
        for i in range(10):
            send("numlock")
            send(70)
            sleep(0.15)
            send("capslock")
            sleep(0.15)

if __name__ == "__main__":
    main()
