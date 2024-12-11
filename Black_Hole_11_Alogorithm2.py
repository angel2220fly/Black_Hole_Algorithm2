def generate_headings_and_variations():
    """
    Generate headings with exactly 128 8-bit variations for each heading:
    - 8-bit variations are reused cyclically across headings.
    - Each heading gets distinct variations, but variations may repeat across headings.
    """
    total_8bit_values = 256  # Number of possible 8-bit values
    variations_per_heading = 128  # Variations allocated per heading
    max_headings = 2 ** 17  # Total number of headings (131,071)

    all_variations = list(range(total_8bit_values))  # All possible 8-bit values

    for heading in range(max_headings):
        heading_bits = f"{heading:017b}"  # Convert heading to 17-bit binary format

        # Cycle through the variations for the current heading
        start_index = (heading * variations_per_heading) % total_8bit_values
        variations_8_bits = [
            all_variations[(start_index + i) % total_8bit_values]
            for i in range(variations_per_heading)
        ]

        for variation in variations_8_bits:
            variation_bits_8 = f"{variation:08b}"  # Convert to 8-bit binary format
            variation_bits_7 = f"{variation % 128:07b}"  # Generate 7-bit variation
            print(f"{heading_bits} {variation_bits_8} {variation_bits_7}")

        print()  # Blank line for separation between headings


# Run the function to print the output
generate_headings_and_variations()