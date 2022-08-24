import re

import subprocess

from random import choice, randint

print("Enter 1 for manual mac changer and 2 for random mac changer: ")

changer = input()
interface = input("Enter your network interface: ").strip()


def main():
    if changer == "1":
        mac = input("Enter the  mac address you want to change: ").strip()
        change_mac(interface, mac)

    elif changer == "2":
        random = mac_random()
        print(random)
        change_mac(interface, random)


def mac_random():
    mac_r = ["00", "40", "96"]
    mac_r2 = ["00", "14", "22"]

    mac_add = choice([mac_r, mac_r2])

    for x in range(3):
        ran_one = choice(str(randint(0, 9)))
        ran_two = choice(str(randint(0, 9)))
        ran_three = (str(ran_one + ran_two))
        mac_add.append(ran_three)

    return ":".join(mac_add)


def change_mac(interface, mac):
    subprocess.call(["ifconfig " + str(interface) + " down"], shell=True)
    subprocess.call(["ifconfig " + str(interface) + " hw ether " + str(mac) + " "], shell=True)
    subprocess.call(["ifconfig " + str(interface) + " up"], shell=True)


# this change_mac changes the mac address manually

def current_mac():
    output = subprocess.check_output(["ifconfig " + "wlan0"], shell=True)

    mac_addy = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))

    print("The  mac address is {}".format(mac_addy))


# current_mac brings up the mac address your machine as seen in ifconfig in the terminal

if __name__ == "__main__":
    main()

# subprocess for executing commands in the terminal/shell
