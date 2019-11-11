from Employee import *


def main():
    read_file()
    display_menu()
    menu_select = input_control("Enter an option from the menu:\t", int, 1)
    menu_nav(menu_select)


def display_menu():
    print("\n" + "*" * 76, "{:>16}".format("MENU"),
          "{:>3}".format("1) Summary"),
          "{:>3}".format("2) Employee Details"),
          "{:>3}".format("3) Total Salary Bill"),
          "{:>3}".format("4) Average Salary"),
          "{:>3}".format("5) Add New Employee"),
          "{:>3}".format("6) Delete Employee"),
          "{:>3}".format("7) Employees by Position"),
          "{:>3}".format("8) Salary Threshold"),
          "{:>3}".format("9) Quit"), sep="\n", end="\n")


def menu_nav(n):
    while n != '9':
        if n == '1':
            total_employees()
        elif n == '2':
            all_employees()
        elif n == '3':
            total_salary()
        elif n == '4':
            average_salary()
        elif n == '5':
            add_employee()
        elif n == '6':
            delete_employee()
        elif n == '7':
            query_position()
        elif n == '8':
            query_threshold()
        elif n == '9':
            break
        else:
            print("INPUT ERROR: Not a valid option from the menu.")

        print("\n"+"*"*76+"\n")
        show_menu = input_control("Show menu? [Y/N]:\t", str, 1)
        if show_menu in ['Y', 'y']:
            display_menu()
            n = input_control("\nEnter an option from the menu:\t", int, 1)
        elif show_menu in ['N', 'n']:
            n = input_control("\nEnter an option from the menu:\t", int, 1)

    print("Any unsaved changes will be lost.")
    sure = input_control("Are you sure you want to quit? [Y/N]:\t", str, 1)

    if sure in ['Y', 'y']:
        print("QUITTING THE PROGRAM . . .")
    elif sure in ['N', 'n']:
        menu_select = input_control("Enter an option from the menu:\t", int, 1)
        menu_nav(menu_select)


def read_file():
    f = open("Employee Deets.txt", "r")
    for line in f.readlines()[1:]:
        record = line.rstrip().split('\n')
        for attributes in record:
            data = attributes.rstrip().split(', ')
            Employee(data[0], data[1], data[2], data[3], data[4], data[5])
    f.close()


def total_employees():
    counter = 0
    for employees in Employee:
        counter += 1
    print("There are {} record(s) in the system.".format(counter))
    return counter


def all_employees():
    for employee in Employee:
        print(employee.enum, employee.name, employee.age, employee.position, employee.salary, employee.years)


def total_salary():
    total = 0
    for employee in Employee:
        total += int(employee.salary)
    print("The total salary bill is: £{}".format(total))
    return total


def average_salary():
    avg = total_salary()/total_employees()
    print("The average salary is: £{}".format(avg))


def add_employee():
    new_num = input_control("Num:\t")
    new_name = input_control("Employee Name:\t")
    new_age = input_control("Employee Age:\t")
    new_position = input_control("Employee Position:\t")
    new_salary = input_control("Employee Salary:\t£")
    new_years = input_control("Employee Years Employed:\t")

    Employee(new_num, new_name, new_age, new_position, new_salary, new_years)


def delete_employee():
    search = input_control("Search for Employee Number:\t")
    found = False
    while found != True:
        for count, employee in enumerate(Employee):
            if employee.enum == search:
                print("Employee {} found!".format(employee.enum))
                employee.deleterecord(count)
                found = True
            else:
                count += 1
                if count == total_employees():
                    print("Record not found, try again.")
                    break


def query_position():
    pass


def query_threshold():
    pass


def input_control(inp, dt=None, lim=None):
    while True:
        ui = input(inp)
        if inp == 'Num:\t' and (len(ui) != 3):
            if len(ui) != 3:
                print("Must be 3 characters long.")
                continue
        if '[Y/N]:\t' in inp:
            if ui not in ['Y', 'y', 'N', 'n']:
                print("Please enter [Y] or [N].")
                continue
        if lim is not None and len(ui) > lim:
            print("Max {} character(s) allowed.".format(lim))
            continue
        if dt is not None:
            if dt == int and not all(nums.isdigit() for nums in ui):
                print("Only numbers accepted in this field.")
                continue
            elif dt == str and not all(chars.isalpha() or chars.isspace()
                                       for chars in ui):
                print("Only letters and spaces accepted in this field.")
                continue
        return ui


main()
