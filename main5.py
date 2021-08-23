#   ESA calculator program by Amogh ASV, Alokpunj bagrodia
#   Takes in details of the students, calculates the average in all aspects and
#   hands out a menu with which the data can be extracted.
#   The program is modular, you can import it.


import time
import os


# Function that does the calculations needed and stores it in a dictionary
def calculator(isa_1, isa_2, esa, name, student_class, student_SRN):
    results = {}
    isa_1_sum = 0
    isa_2_sum = 0
    esa_sum = 0
    total = 30
    isa_1_relative = []
    isa_2_relative = []
    esa_relative = []
    for i in range(len(isa_1)):
        isa_1_sum += isa_1[i] / 2
        isa_2_sum += isa_2[i] / 2
        esa_sum += esa[i] / 2
        if i == 2:
            total = 45 / 2
        else:
            pass
        isa_1_relative.append(f"{(isa_1[i] / 2) / total:04}%")
        isa_2_relative.append(f"{(isa_1[i] / 2) / total:04}%")
        esa_relative.append(f"{(esa[i] / 2) / total}%")

    # Writing the values into a dictionary (results).

    results["name"] = name
    results["class"] = student_class
    results["Student SRN"] = student_SRN.upper()

    results["ISA 1 marks"] = isa_1
    results["ISA 2 marks"] = isa_2
    results["ESA marks"] = esa

    results["ISA 1 total relative"] = isa_1_sum
    results["ISA 2 total relative"] = isa_2_sum
    results["ESA total relative"] = esa_sum

    results["ISA 1 relative"] = isa_1_relative
    results["ISA 2 relative"] = isa_2_relative
    results["ESA relative"] = esa_relative

    results["ISA 1 average"] = f"{(isa_1_sum / 150) * 100:04}%"
    results["ISA 2 average"] = f"{isa_2_sum / 120:04}%"
    results["ESA average"] = f"{esa_sum / 222.5:04}%"

    results["Total average"] = (isa_2_sum + isa_1_sum + esa_sum) / (120 + 150 + 222.5)

    return results


# Accepts a dictionary as an argument and creates a menu of keys that can be viewed
def output(results: dict):
    while True:
        print("Enter the number corresponding to the details you want to see (e/exit to exit): ")
        i = 1
        keys_results = []

        # Printing the list of options (keys) possible
        for element in results:
            print(f"{i}) {element}")
            keys_results.append(element)
            i += 1

        choice = input("=>")
        if choice.lower() == "e" or choice.lower() == "exit":
            choice_2 = input("Do you want to store the details?(y/yes/n/no): ")
            if choice_2.lower() == "y" or choice_2.lower() == "yes":

                # Checking and creating folders necessary for writing to file
                if not os.path.isdir("./details"):
                    os.mkdir("./details")
                if not os.path.isdir(f"./details/{results['class'].upper()}"):
                    os.mkdir(f"./details/{results['class'].upper()}")
                with open(f"./details/{results['class'].upper()}/{results['name'].lower().replace(' ', '_')}.txt", "w",
                          encoding="utf-8") as file_handle:
                    for i in range(results.__len__()):

                        # Writing to the file in the format of key: value
                        if isinstance(results[keys_results[i]], list):
                            file_handle.write(f"{keys_results[i]}: ")
                            file_handle.write("".join(str(results[keys_results[i]])))
                            file_handle.write("\n")
                        else:
                            file_handle.write(f"{keys_results[i]}: {results[keys_results[i]]}\n")
                print(
                    f"Saved data to \"./details/{results['class'].upper()}/{results['name'].lower().replace(' ', '_')}.txt\" ")
                break
            else:
                break
        else:
            if choice.isdigit():
                if 1 <= int(choice) <= i - 1:
                    # Prints the details in the format of "key: value"
                    if isinstance(results[keys_results[int(choice) - 1]], list):
                        print(f"{keys_results[int(choice) - 1]}: ", end="")
                        print(", ".join(results[keys_results[int(choice) - 1]]))
                    else:
                        print(f"{keys_results[int(choice) - 1]}: {results[keys_results[int(choice) - 1]]}")
                    input("Press any key to continue...")
                else:
                    print(f"Please enter a value between 0 and {i - 1}, {choice} is not valid")
                    _ = input("Press any key to continue...")
            else:
                print(f"Please enter values between 0 and {i - 1}")
                _ = input("Press any key to continue")

        # Clears the screen

        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
        else:
            pass


# Takes ESA marks from the student
def esa_input():
    esa = []
    i = 0
    subject_list = ["Constitution", "Computer Science", "Mechanics", "Chemistry", "Electronics", "Mathematics"]
    print("Enter the ESA marks of the following subjects:")
    while i < len(subject_list):
        try:
            value = float(input(f"{subject_list[i]}: "))
            if subject_list[i] == "Constitution":
                if 0 <= value <= 45:
                    esa.append(value)
                    if i >= 0:
                        i += 1
                else:
                    print("Please enter a value between 0 and 45")
            else:
                if 0 <= value <= 100:
                    esa.append(value)
                    if i >= 0:
                        i += 1
                else:
                    print("Please enter a value between 0 and 100")
        except ValueError:
            print("Please enter real numbers only")

    return esa


# Takes ISA 1 inputs from the user
def isa_1_input():
    isa_1 = []
    i = 0
    subject_list = ["Constitution", "Computer Science", "Mechanics", "Chemistry", "Electronics", "Mathematics"]
    print("Enter the ISA 1 marks of the following subjects:")
    while i < len(subject_list):
        try:
            value = float(input(f"{subject_list[i]}: "))
            if subject_list[i] == "Constitution":
                if 0 <= value <= 45:
                    isa_1.append(value)
                    if i >= 0:
                        i += 1
                else:
                    print("Please enter a value between 0 and 45 for Constitution")
            else:
                if 0 <= value <= 60:
                    isa_1.append(value)
                    if i >= 0:
                        i += 1
                else:
                    print("Please enter a value between 0 and 60")

        except ValueError:
            print("Please enter only real numbers")

    return isa_1


# Takes ISA 2 inputs from the user
def isa_2_input():
    isa_2 = []
    i = 0
    subject_list = ["Constitution", "Computer Science", "Mechanics", "Chemistry", "Electronics", "Mathematics"]
    print("Enter the ISA 2 marks of the following subjects:")
    while i < len(subject_list):
        try:
            value = float(input(f"{subject_list[i]}: "))
            if subject_list[i] == "Constitution":
                if 0 <= value <= 30:
                    isa_2.append(value)
                    if i >= 0:
                        i += 1
                else:
                    print("Please enter a value between 0 and 30 for constitution")
            else:
                if 0 <= value <= 40:
                    isa_2.append(value)
                    if i >= 0:
                        i += 1
                else:
                    print("Please enter a value between 0 and 40")

        except ValueError:
            print("Please enter only real numbers")

    return isa_2


# Driver function
def main():
    print("ESA calculator")

    name = input("Enter the name of the student: ")
    student_class = input("Enter the class: ")
    student_SRN = input("Enter the SRN of the user: ")
    print("*****************************************************************")
    print()

    isa_1 = isa_1_input()
    print("*****************************************************************")
    print()

    isa_2 = isa_2_input()
    print("*****************************************************************")
    print()

    esa = esa_input()
    results = calculator(isa_1, isa_2, esa, name, student_class, student_SRN)
    print("*****************************************************************")
    print("Inputs have been taken!")
    time.sleep(3)

    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        pass

    output(results)


if __name__ == "__main__":
    main()