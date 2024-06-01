import os

def generate_tree(root_dir: str, prefix: str="") -> None:
    """
    Recursively prints the folder structure.
    
    Args:
        root_dir (str): The root directory to start generating the tree from.
        prefix (str, optional): The prefix to use for each level of the tree. Defaults to an empty string.
    """
    
    files = os.listdir(root_dir)
    # Filter to exclude hidden files and folders
    files = [f for f in files if not f.startswith('.')]
    entries = [os.path.join(root_dir, f) for f in files]
    # Sort directories first
    entries.sort(key=lambda x: (not os.path.isdir(x), x))
    for i, entry in enumerate(entries):
        is_last = i == (len(entries) - 1)
        more = '└──' if is_last else '├──'
        print(f"{prefix}{more} {os.path.basename(entry)}/" if os.path.isdir(entry) else f"{prefix}{more} {os.path.basename(entry)}")
        # Print comment space if it's a folder
        if os.path.isdir(entry):
            print(f"{prefix}{'    ' if is_last else '│   '}# Add comments here")
            new_prefix = prefix + ('    ' if is_last else '│   ')
            generate_tree(entry, new_prefix)

# Get the current working directory (cwd)
cwd = os.getcwd()
print(f"{os.path.basename(cwd)}/")
print("# Root of the project")
generate_tree(cwd)

# Add message after processing
print("""\n\nCopy the created folder structure from the console
and paste it into the file 'folder_structure.txt'.""")