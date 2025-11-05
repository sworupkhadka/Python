# Define the placeholder text that will be replaced with actual names
PLACEHOLDER = "[name]"

# Read the list of names from the input file
with open("./input/names/invited_name.txt") as name_file:
    # Read all names into a list (each line becomes a list item)
    names = name_file.readlines()
    print(names)

# Read the template letter from the input file
with open("input/letters/starting_letter.txt") as letter_file:
    # Read the entire letter template as a string
    letter = letter_file.read()

    # Process each name in the list
    for name in names:
        # Remove any whitespace or newline characters from the name
        stripped_name = name.strip()

        # Replace the placeholder with the current name
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        print(new_letter)  # Debug: Print the personalized letter

        # Create a new file for each personalized letter
        with open(f"./output/ReadyToSend/Letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            # Write the personalized letter to the new file
            completed_letter.write(new_letter)