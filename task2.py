# Task 2: Write and Append Data to a File


data = input("Enter some text to write into the file: ")

file = open("output.txt", "w")
file.write(data + "\n")
file.close()

print("Data successfully written to output.txt")


additional_data = input("Enter additional text to append: ")


file = open("output.txt", "a")
file.write(additional_data + "\n")
file.close()

print("Data successfully appended.")


file = open("output.txt", "r")

print("\nFinal content of output.txt:")

content = file.read()
print(content)

file.close()