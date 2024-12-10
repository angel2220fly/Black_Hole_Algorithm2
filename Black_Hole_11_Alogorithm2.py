def generate_headings_and_variations():
    """
    #Created by Jurijus Pacalovas.
    Generate headings in the range 0 to 65535 (16-bit), and for each heading,
    generate 128 variations with 8 bits from 0-127, and 128 variations with 8 bits
    from 255-127. Each variation is printed in one line with heading, 8-bit, and 7-bit.
    """
    # First range of headings: 0 to (2^16)-1 (0-65535)
    max_heading_1 = (2 ** 16)

    # Second range of headings: (2^16) to (2^17)-1 (65536-131070)
    max_heading_2 = (2 ** 17)
    
    # First set of headings (0 to 65535)
    for heading in range(max_heading_1):
        heading_bits = f"{heading:016b}"  # Convert heading to 16-bit binary format

        # Generate 128 variations (0-127) for the first set
        variations_8_bits = list(range(128))

        for i, variation in enumerate(variations_8_bits):
            variation_bits_8 = f"{variation:08b}"  # 8-bit variation

            # Generate 7-bit variation for the first 128 variations only
            variation_bits_7 = f"{variation:07b}"  # 7-bit variation
            print(f"{heading_bits} {variation_bits_8} {variation_bits_7}")
        
        print()  # Blank line for separation between headings
    
    # Second set of headings (65536 to 131070)
    for heading in range(max_heading_1, max_heading_2):
        heading_bits = f"{heading:017b}"  # Convert heading to 17-bit binary format

        # Generate 128 variations (255-127) for the second set
        variations_8_bits = list(range(255, 127, -1))

        for i, variation in enumerate(variations_8_bits):
            variation_bits_8 = f"{variation:08b}"  # 8-bit variation

            # Generate 7-bit variation for the first 128 variations only
            variation_bits_7 = f"{variation % 128:07b}"  # 7-bit variation within range 0-127
            print(f"{heading_bits} {variation_bits_8} {variation_bits_7}")
        
        print()  # Blank line for separation between headings


# Run the function to print the output
generate_headings_and_variations()