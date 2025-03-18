def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes it to a new file.

    Args:
        input_filename: The name of the input file.
        output_filename: The name of the output file.
    """
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                # Example modification: Uppercase each line
                modified_line = line.upper()
                outfile.write(modified_line)
        print(f"File '{input_filename}' modified and written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except IOError:
        print(f"Error: An I/O error occurred while processing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_filename_from_user():
    """
    Asks the user for a filename and handles potential errors.
    """
    while True:
        filename = input("Enter the filename: ")
        try:
            with open(filename, 'r'): #try opening to see if it exists and is readable.
                print(f"File '{filename}' exists and is readable.")
                return filename
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except IOError:
            print(f"Error: File '{filename}' is not readable.")

# Main program
input_filename = get_filename_from_user()
output_filename = "modified_" + input_filename  # Create a new filename
modify_and_write_file(input_filename, output_filename)