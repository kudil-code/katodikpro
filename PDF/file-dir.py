import os

def create_file_structure_md(output_filename="file_structure.md"):
    """
    Scans the current directory and its subdirectories, then writes
    the names of all files and directories to a Markdown file.
    """
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write("# File and Directory Structure\n\n")
        f.write("This file lists all files and directories found in the current path.\n\n")

        for root, dirs, files in os.walk('.'):
            # Calculate the current depth for indentation
            level = root.replace('./', '').count(os.sep)
            indent = '    ' * level

            # Write directory names
            for d in dirs:
                f.write(f"{indent}- **{d}/**\n")

            # Write file names
            for file in files:
                f.write(f"{indent}- {file}\n")

if __name__ == "__main__":
    create_file_structure_md()
    print("File structure has been saved to file_structure.md")