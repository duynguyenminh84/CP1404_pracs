"""Estimated Time: 120 minutes"""

import csv

from prac_07.project import Project

welcome_message = "Welcome to Pythonic Project Management"
menu = "_ (L)oad Projects\n_ (S)ave projects\n_ (D)isplay projects  \n_ (F)ilter projects by date\n_ (A)dd new project\n_ (U)pdate project\n_ (Q)uit"
def main():


    print(welcome_message)
    with open('projects.txt') as f:
        lines = len(f.readlines())
        print("Loading " + str(lines -1) + " projects from projects.txt")

    print(menu)
    selection = input(">>> ")
    selection = selection.upper()
    """Menu choice for users"""
    while selection != "Q":

        if selection == "L":
            load_projects()
            print(menu)
            selection = input(">>> ")
            selection = selection.upper()

        elif selection == "S":
            pass
            print(menu)
            selection = input(">>> ")
            selection = selection.upper()

        elif selection == "D":
            display_projects()
            print(menu)
            selection = input(">>> ")
            selection = selection.upper()
        elif selection == "F":
            pass
            print(menu)
            selection = input(">>> ")
            selection = selection.upper()
        elif selection == "A":
            pass
            print(menu)
            selection = input(">>> ")
            selection = selection.upper()
        elif selection == "U":
            update_project()
            print(menu)
            selection = input(">>> ")
            selection = selection.upper()

        else:
            print("Invalid menu choice")
            print(menu)
            selection = input(">>> ")
            selection = selection.upper()





def load_projects():

    Projects = []

    # open the file for reading
    in_file = open('projects.txt', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip("\n").split('\t')
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        Projects.append(project)
    in_file.close()
    for project in Projects:
        print(project)

def display_projects():
    Projects = []
    # open the file for reading
    in_file = open('projects.txt', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip("\n").split('\t')
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        Projects.append(project)
    in_file.close()

    print("Incomplete project:")
    Projects.sort()
    for project in Projects:
        if int(project.status) != 100:
            print(project)

    print("Complete project:")
    for project in Projects:
        if int(project.status) == 100:
            print(project)


def update_project():
    Projects = []
    # open the file for reading
    in_file = open('projects.txt', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip("\n").split('\t')
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        Projects.append(project)
    in_file.close()

    for project in Projects:
        print(str(Projects.index(project))+" " + str(project))
    choice = int(input("Project choice:"))
    print(Projects[choice])
    new_percentage = int(input("New percentage:"))
    new_priority = int(input("New priority:"))

    with open("projects.txt") as file:
        contents = file.read()
        contents = contents.replace(Projects[choice].status, str(new_percentage))
    with open("projects.txt", "w") as file:
        file.write(contents)


if __name__ == '__main__':
    main()








