import random

def generate_headings_and_variations():
    """
    Generate headings in two distinct ranges:
    1. 0 to (2^16)-1 (0-65535) with 128 unique 8-bit variations from 0-255.
    2. (2^16) to (2^17)-1 (65536-131070) with 128 unique 8-bit variations from 255-127.
    Ensure all 8-bit variations are unique within each heading range.
    """
    # First range of headings: 0 to (2^16)-1 (0-65535)
    for heading in range(2 ** 16):
        heading_bits = f"{heading:017b}"  # Convert heading to 17-bit binary format

        # Generate 128 unique variations from 0 to 127
        variations_8_bits = random.sample(range(256), 128)

        for variation in variations_8_bits:
            variation_bits_8 = f"{variation:08b}"  # Convert to 8-bit binary format
            variation_bits_7 = f"{variation % 128:07b}"  # Generate 7-bit variation
            print(f"{heading_bits} {variation_bits_8} {variation_bits_7}")
        
        print()  # Blank line for separation between headings

    # Second range of headings: (2^16) to (2^17)-1 (65536-131070)
    for heading in range(2 ** 16, 2 ** 17):
        heading_bits = f"{heading:017b}"  # Convert heading to 17-bit binary format

        # Generate 128 unique variations from 255 to 127
        variations_8_bits = random.sample(range(128, 256), 128)

        for variation in variations_8_bits:
            variation_bits_8 = f"{variation:08b}"  # Convert to 8-bit binary format
            variation_bits_7 = f"{variation % 128:07b}"  # Generate 7-bit variation (modulo to fit range)
            print(f"{heading_bits} {variation_bits_8} {variation_bits_7}")
        
        print()  # Blank line for separation between headings


# Run the function to print the output
generate_headings_and_variations()