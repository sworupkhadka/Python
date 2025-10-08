def calculate_love_score(name1, name2):
    # Combine both names into a single string
    # Convert to lowercase so the letter counting is case-insensitive
    combined_names = (name1 + name2).lower()

    # Count occurrences of letters in the word "TRUE"
    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    true_score = t + r + u + e  # Total count for "TRUE"

    # Count occurrences of letters in the word "LOVE"
    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")
    love_score = l + o + v + e  # Total count for "LOVE"

    # Combine both scores to form a two-digit number (as string first, then to int)
    total_score = int(str(true_score) + str(love_score))

    # Display the final love score
    print(total_score)


#Test the function with sample names
calculate_love_score("Kanye West", "Kim Kardashian")
