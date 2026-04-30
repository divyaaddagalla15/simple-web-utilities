import os

def clean_filenames(directory):
    print(f"Scanning: {directory}")
    for filename in os.listdir(directory):
        # Example: Replace spaces with underscores and make lowercase
        new_name = filename.replace(" ", "_").lower()
        
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        
        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")

# To use: clean_filenames("path_to_your_folder")
print("This script is ready to organize your local files!")
