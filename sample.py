import argparse

def analyze_anxiety(age, sleep, stress):
    # Simple heuristic for demonstration
    if stress > 7 or sleep < 5:
        result = "High Anxiety"
    else:
        result = "Low Anxiety"
    return result

# Create the parser
parser = argparse.ArgumentParser(description="Anxiety Prediction System")

# Add arguments
parser.add_argument('--age', type=int, required=True, help="Age of the user")
parser.add_argument('--sleep', type=int, required=True, help="Hours of sleep per night")
parser.add_argument('--stress', type=int, required=True, help="Stress level (1-10)")

# Parse the arguments
args = parser.parse_args()

# Analyze anxiety
result = analyze_anxiety(args.age, args.sleep, args.stress)

# Display the result
print(f"Anxiety Analysis Result: {result}")