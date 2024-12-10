def generate_headings_and_variations():
    """
    Generate headings in the range 0 to 131,070 (17-bit), and for each heading,
    generate 256 variations with 8 bits and 128 variations with 7 bits.
    Ensure 8-bit variations are unique, with repeats two times: first in order (0-255),
    then in reverse (255-0). Each variation is printed in one line with heading, 8-bit, and 7-bit.
    """
    max_headings = (2 ** 17)  # Total headings: 131,071 (0 to 131,070)

    for heading in range(max_headings):
        heading_bits = f"{heading:017b}"  # Convert heading to 17-bit binary format

        # Generate 256 variations (first 0-255, then 255-0)
        variations_8_bits = list(range(256)) + list(reversed(range(256)))

        for i, variation in enumerate(variations_8_bits):
            variation_bits_8 = f"{variation:08b}"  # 8-bit variation

            # Generate 7-bit variation (for the first 128 of the 256 variations)
            if i % 256 < 128:  # First 128 variations only
                variation_bits_7 = f"{variation % 128:07b}"  # Ensure 7-bit range
                print(f"{heading_bits} {variation_bits_8} {variation_bits_7}")
            else:
                print(f"{heading_bits} {variation_bits_8} ---")  # Placeholder for no 7-bit variation

        print()  # Blank line for separation between headings


# Run the function to print the output
generate_headings_and_variations()