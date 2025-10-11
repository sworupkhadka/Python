# Define a function that returns multiple values


def get_name_details(first_name, last_name):
    # Convert names to different formats
    full_name = f"{first_name.title()} {last_name.title()}"
    initials = f"{first_name[0].upper()}.{last_name[0].upper()}."
    
    # Return both values
    return full_name, initials

# Call the function and unpack the returned values
name, short = get_name_details("sworup", "khadka")

# Print the results
print("Full Name:", name)
print("Initials:", short)
