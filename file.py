import sys
def process_file(dub:str):
    try:
        with open(dub, 'r') as file:
            line_number = 1
            for line in file:
                values = line.strip().split()

                if len(values) != 2:
                    print(f"Error on line {line_number}: Expected two values but found {len(values)}.")
                else:
                    try:
                        num1 = float(values[0])
                        num2 = float(values[1])
                        print(f"Sum on line {line_number}: {num1 + num2}")
                    except ValueError:
                        print(f"Error on line {line_number}: Could not convert one or both values to floats.")

                line_number += 1

    except FileNotFoundError:
        print(f"Error: The file '{dub}' could not be opened.")
        sys.exit(1)

if __name__ == "__main__":
    # Check for command-line argument
    if len(sys.argv) != 2:
        print("Error: Please provide the filename as a single command-line argument.")
        sys.exit(1)

    # Run the function with the provided filename
    process_file(sys.argv[1])


