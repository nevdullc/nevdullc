#!/usr/bin/env python3
"""Linux Command Stash v.1 :: nevdullc :: 20220629"""

# imports
import glob
import os
import re
import sys

# add_cmd : add additional commands to the cmd_stash.txt list appended by a newline
def add_cmd():
    with open("cmd_list.txt", "a") as cmd_list:
        print("Add a command .. ")
        ans = True
        while ans == True:
            new_cmd = str(input("Enter new command to append to Command list : "))
            cmd_list.write(str(new_cmd))
            cmd_list.write(str('\n'))
            cont = str(input("Add another command.. (y/n, m for menu ? :"))
            if cont == 'n':
                cmd_list.close()
                ans = False
            elif cont == 'm':
                cmd_list.close()
                ans = False
    
    cmd_menu()

# cmd_menu : main menu of the Linux Command Stash (cmd_stash.py), commands are stored in cmd_stash.txt
def cmd_menu():
    os.system('clear')
    
    menu_opt = str(input('''
    Linux Command Stash :: v 1.0 nevdullc::2022

    Please choose from the options 1, 2, 3 or q to quit :

    1.) add command to the list
    2.) search for commands in list
    3.) print entire command list 
    q.) Quit

    '''))

    if menu_opt == "1":
        add_cmd() 
    elif menu_opt == "2":
        grep_cmd()
    elif menu_opt == "3":
        list_cmd()
    elif menu_opt == "q":
        exit()

# grep_cmd : search for a string from the cmd_stash.txt file and display any matches
def grep_cmd():
    gcmd = str(input("Search for : "))
    with open("cmd_list.txt", "r") as cmd_list:
        for cmd in cmd_list:
            if re.search(gcmd, cmd):
                print(cmd)

    x = input("Press Enter to continue.. ")
    cmd_menu()

# list_cmd : list all commands in the cmd_stash.txt sorted alphabetically
def list_cmd():
    with open("cmd_list.txt", "r") as cmd_list:
        cmds = cmd_list.readlines()
        cmds.sort()
        for cmd in cmds:
            print(cmd)

    x = input("Press Enter to continue.. ")
    cmd_menu()

# main <--
def main():
    cmd_menu()

# name space main <--
if __name__ == '__main__':
    main()

