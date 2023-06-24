def write_data(file="data.txt"):
    roll_no = input("Enter your roll number: ")
    name = input("Enter your name: ")
    class_name = input("Enter your class: ")

    # Open the file in append mode
    file_object = open(file, "a")

    # Write data to the file
    file_object.writelines(roll_no + "\n")
    file_object.writelines(name + "\n")
    file_object.writelines(class_name + "\n")

    # Close the file
    file_object.close()

    # Open the file again in read mode
    file_object = open(file, "r")

    # Read and print the data
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())

    # Close the file
    file_object.close()


# Test the function
write_data()