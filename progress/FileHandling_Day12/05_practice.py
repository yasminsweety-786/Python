note = input("Enter a note: ")

file = open("notes.txt", "a")

file.write(note + "\n")

file.close()

print("Note saved successfully!")