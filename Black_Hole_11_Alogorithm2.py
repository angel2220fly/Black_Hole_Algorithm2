import random

def generate_headings_and_variations():
    """
    #Created by Jurijus Pacalovas.
    Generate 2^17 (131,072) headings, where each heading has:
    - 128 unique 8-bit variations generated using PRNG (pseudo-random number generator).
    - The first 64 variations are in normal order.
    - The next 64 variations are the reverse of the first 64.
    Each line includes a 17-bit heading, 8-bit variation, and a 7-bit version.
    """
    max_headings = 2 ** 17  # Total number of headings
    variations_per_heading = 128  # Variations allocated per heading
    half_variations = variations_per_heading // 2  # Half of the variations (64)
    
    random.seed(42)  # Seed for reproducibility
    
    for heading in range(max_headings):
        heading_bits = f"{heading:017b}"  # Convert heading to 17-bit binary format

        # Generate the first half (64 unique PRNG-based variations)
        first_half = random.sample(range(256), half_variations)

        # Create the second half as the reverse of the first half
        second_half = list(reversed(first_half))

        # Combine both halves
        variations_8_bits = first_half + second_half

        for variation in variations_8_bits:
            variation_bits_8 = f"{variation:08b}"  # Convert to 8-bit binary format
            variation_bits_7 = f"{variation % 128:07b}"  # Generate 7-bit variation
            print(f"{heading_bits} {variation_bits_8} {variation_bits_7}")

        print()  # Blank line for separation between headings


# Run the function to print the output
generate_headings_and_variations()