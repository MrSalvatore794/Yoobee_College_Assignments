
def process_junk_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    # number of lines
    total_lines = len(lines)
    print(f"Total number of lines in the original file: {total_lines}")
    
    # Convert all text to lowercase
    lowercase_lines = []
    for line in lines:
        lowercase_lines.append(line.lower())
        
    if lowercase_lines and not lowercase_lines[-1].endswith('\n'):
        lowercase_lines[-1] += '\n'
        
    lowercase_lines.append("text file analysis\n")
    
    # Save the processed file
    
    with open(file_path, 'w') as file:
        file.writelines(lowercase_lines)
        
    print("File successfully processed and saved!")

    # Run
if __name__ == '__main__':
    process_junk_file("junk.txt")