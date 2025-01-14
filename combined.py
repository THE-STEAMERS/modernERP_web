import os

# Set the directory containing the code files
code_directory = r'D:\hack\modernERP'  # Replace with your actual path

# Specify the output file
output_file = 'combined_code.txt'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Walk through the directory
    for root, dirs, files in os.walk(code_directory):
        for file in files:
            # Check for code file extensions
            if file.endswith(('.js', '.py', '.java', '.cpp', '.ts', '.jsx', '.tsx')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as infile:
                    # Write the file name as a header
                    outfile.write(f'\n\n// File: {file_path}\n\n')
                    # Write the contents of the file
                    outfile.write(infile.read())
