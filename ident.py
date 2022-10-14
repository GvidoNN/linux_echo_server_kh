import csv
import os

def write_user(addr, name, password):
    with open("users.csv", "a", encoding="utf-8", newline="") as file:
        print(f"Start writing {addr}, {name}, {password}")
        writer = csv.writer(file)
        writer.writerow((addr, name, password))

def check_user(addr, name, password):
    with open("users.csv", "r", encoding="utf-8", newline="") as file: 
            reader = csv.reader(file)
            
            incorrect = 0
            correct = 0

            for row in reader:
                if os.stat("users.csv").st_size != 0:
                #if addr ==row[0]:
                    if addr == row[0] and name == row[1] and password == row[2]:
                        print(f"Hello, {row[1]}!")
                        correct = 1
                        break
                    elif addr == row[0] and name == row[1]:
                        print('Incorrect name or password')
                        incorrect = 1
                

            if not(incorrect or correct):
                print("Not found this name")
                write_user(addr, name, password)




