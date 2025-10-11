# Define a function to format first and last name
def format_name(f_name, l_name):
    # Convert first name to title case (e.g. sworup → Sworup)
    title_case_f = f_name.title()

    # Convert last name to title case (e.g. khadka → Khadka)
    title_case_l = l_name.title()

    # Combine first and last name (currently without a space)
    full_name = f"{title_case_f} {title_case_l}"

    # Print the formatted full name
    print("Full Name in Title Case:", full_name)

# Call the function with example inputs
format_name("sworup", "khadka")
